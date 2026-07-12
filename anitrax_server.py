"""
ANITRAX — Servidor unificado
Puerto: 8001
- ZK Proof Server (Circom/snarkjs)
- Casper Testnet Server
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import hashlib
import subprocess
import time
import uuid
import os
import json
import requests as http_requests

app = FastAPI(title="ANITRAX Unified Server")

# ── Configuración ZK ──────────────────────────────────────────────────────────
ZK_DIR = r"C:\Users\Francisco Almaraz\anitrax-zk"
WASM_PATH = os.path.join(ZK_DIR, "solvencia_js", "solvencia.wasm")
ZKEY_PATH = os.path.join(ZK_DIR, "solvencia_final.zkey")
WITNESS_GEN_SCRIPT = os.path.join(ZK_DIR, "solvencia_js", "generate_witness.js")

# Factor de escala: ETH × 1,000,000 para enteros en Circom
ETH_SCALE = 1_000_000

# ── Configuración Casper ──────────────────────────────────────────────────────
CASPER_PUBLIC_KEY = "02021ece4a3a164adff5b5a1a6614c451dd562783e6ede022cd79d088a63cd66d37f"
PRIVATE_KEY_PATH = r"C:\Users\Francisco Almaraz\casper_private_key.pem"

# Saldo confirmado en testnet.cspr.live — nodo RPC público no disponible
CSPR_BALANCE_FALLBACK = 10.32

# ── Modelos ZK ────────────────────────────────────────────────────────────────

class ProofRequest(BaseModel):
    saldo: float
    monto: float

class ProofResponse(BaseModel):
    valido: bool
    proof_hash: str
    monto_publico: float
    mensaje: str

# ── Modelos Casper ────────────────────────────────────────────────────────────

class EventRequest(BaseModel):
    event_type: str
    event_data: str
    metadata: Optional[str] = ""

class EventResponse(BaseModel):
    success: bool
    event_id: str
    event_hash: str
    deploy_hash: Optional[str] = None
    timestamp: int
    message: str
    explorer_url: Optional[str] = None
    mode: str

class BalanceResponse(BaseModel):
    public_key: str
    balance_cspr: float
    balance_motes: int

# ── Helpers ZK ────────────────────────────────────────────────────────────────

def run_zk_proof(saldo: float, monto: float) -> str:
    saldo_int = int(round(saldo * ETH_SCALE))
    monto_int = int(round(monto * ETH_SCALE))

    if monto_int > saldo_int:
        raise ValueError(
            f"Monto ({monto} = {monto_int}) excede saldo ({saldo} = {saldo_int})"
        )

    work_id = str(uuid.uuid4())[:8]
    work_dir = os.path.join(ZK_DIR, f"_tmp_{work_id}")
    os.makedirs(work_dir, exist_ok=True)

    input_path   = os.path.join(work_dir, "input.json")
    witness_path = os.path.join(work_dir, "witness.wtns")
    proof_path   = os.path.join(work_dir, "proof.json")
    public_path  = os.path.join(work_dir, "public.json")

    try:
        with open(input_path, "w") as f:
            json.dump({"saldo": str(saldo_int), "monto": str(monto_int)}, f)

        r = subprocess.run(
            ["node", WITNESS_GEN_SCRIPT, WASM_PATH, input_path, witness_path],
            capture_output=True, text=True, timeout=30
        )
        if r.returncode != 0:
            raise Exception(f"Error generando witness: {r.stderr}")

        r = subprocess.run(
            ["snarkjs", "groth16", "prove", ZKEY_PATH,
             witness_path, proof_path, public_path],
            capture_output=True, text=True, timeout=30, shell=True
        )
        if r.returncode != 0:
            raise Exception(f"Error generando prueba: {r.stderr}")

        with open(proof_path, "rb") as f:
            proof_bytes = f.read()
        return hashlib.sha256(proof_bytes).hexdigest()

    finally:
        for fp in [input_path, witness_path]:
            if os.path.exists(fp):
                try:
                    os.remove(fp)
                except Exception:
                    pass

# ── Helpers Casper ────────────────────────────────────────────────────────────

def generate_event_hash(event_type, event_data, event_id, timestamp):
    payload = f"{event_id}:{event_type}:{event_data}:{timestamp}"
    return hashlib.sha256(payload.encode()).hexdigest()

def get_cspr_balance() -> float:
    """
    Retorna el saldo CSPR confirmado en testnet.cspr.live.
    El nodo RPC público de Casper Testnet no es accesible desde
    esta red — se usa el saldo verificado manualmente: 10.32 CSPR.
    """
    return CSPR_BALANCE_FALLBACK

def has_private_key():
    return os.path.exists(PRIVATE_KEY_PATH)

def send_deploy_demo(event_hash, event_id):
    demo_hash = hashlib.sha256(
        f"DEMO:{event_hash}:{event_id}".encode()
    ).hexdigest()
    return f"demo_{demo_hash}"

def send_deploy_live(event_hash, event_id):
    import pycspr
    from pycspr import crypto
    private_key = crypto.read_private_key(PRIVATE_KEY_PATH, "secp256k1")
    params = pycspr.create_deploy_parameters(
        account=private_key,
        chain_name="casper-test",
        dependencies=[],
        gas_price=1,
        timestamp=pycspr.get_timestamp(),
        ttl="30m"
    )
    correlation_id = int(uuid.UUID(event_id).int % 1_000_000)
    transfer = pycspr.create_transfer(
        params=params,
        correlation_id=correlation_id,
        target=CASPER_PUBLIC_KEY,
        amount=2_500_000_000
    )
    transfer.approve(private_key)
    client = pycspr.NodeClient(pycspr.NodeConnectionInfo(
        host="15.197.132.60", port=7777
    ))
    return str(client.send_deploy(transfer))

# ── Endpoints generales ───────────────────────────────────────────────────────

@app.get("/")
def health():
    return {
        "status": "ANITRAX Unified Server activo",
        "services": ["ZK Proof", "Casper Testnet"],
        "network": "Casper Testnet + Ethereum Sepolia",
        "casper_mode": "live" if has_private_key() else "demo",
        "zk_scale": f"1 ETH = {ETH_SCALE} unidades ZK"
    }

# ── Endpoints ZK ─────────────────────────────────────────────────────────────

@app.post("/generar-prueba", response_model=ProofResponse)
def generar_prueba(req: ProofRequest):
    try:
        proof_hash = run_zk_proof(req.saldo, req.monto)
        return ProofResponse(
            valido=True,
            proof_hash=proof_hash,
            monto_publico=req.monto,
            mensaje="Prueba ZK generada correctamente. El saldo real nunca fue transmitido."
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── Endpoints Casper ──────────────────────────────────────────────────────────

@app.get("/casper/balance", response_model=BalanceResponse)
def get_casper_balance():
    cspr = get_cspr_balance()
    return BalanceResponse(
        public_key=CASPER_PUBLIC_KEY,
        balance_cspr=round(cspr, 4),
        balance_motes=int(cspr * 1_000_000_000)
    )

@app.post("/casper/registrar-evento", response_model=EventResponse)
def registrar_evento(req: EventRequest):
    event_id  = str(uuid.uuid4())
    timestamp = int(time.time())
    event_hash = generate_event_hash(
        req.event_type, req.event_data, event_id, timestamp
    )
    try:
        if has_private_key():
            deploy_hash  = send_deploy_live(event_hash, event_id)
            mode         = "live"
            message      = "Evento registrado en Casper Testnet"
            explorer_url = f"https://testnet.cspr.live/deploy/{deploy_hash}"
        else:
            deploy_hash  = send_deploy_demo(event_hash, event_id)
            mode         = "demo"
            message      = "Hash generado (modo demo — agrega casper_private_key.pem para transacciones reales)"
            explorer_url = None

        return EventResponse(
            success=True,
            event_id=event_id,
            event_hash=event_hash,
            deploy_hash=deploy_hash,
            timestamp=timestamp,
            message=message,
            explorer_url=explorer_url,
            mode=mode
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/casper/deploy/{deploy_hash}")
def consultar_deploy(deploy_hash: str):
    if deploy_hash.startswith("demo_"):
        return {
            "deploy_hash": deploy_hash,
            "status": "demo",
            "message": "Deploy simulado — agrega .pem para transacciones reales"
        }
    return {
        "deploy_hash": deploy_hash,
        "status": "pending",
        "explorer_url": f"https://testnet.cspr.live/deploy/{deploy_hash}"
    }

@app.get("/casper/eventos-tipos")
def get_event_types():
    return {
        "event_types": [
            "transfer_sent", "transfer_received",
            "task_start", "task_end",
            "agent_execution", "automation_complete",
            "audit_log", "workflow_created", "workflow_modified",
            "critical_event", "zk_proof_generated",
            "bluetooth_connected", "voice_command_executed"
        ]
    }