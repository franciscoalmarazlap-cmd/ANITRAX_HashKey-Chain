# 🟣 ANITRAX — AI-Powered Offline-First Financial System

**HashKey Chain On-Chain Horizon Hackathon 2026 — AI & DeFi Tracks**

ANITRAX is a mobile peer-to-peer financial transfer system with an autonomous AI agent, Bluetooth offline transfers, Zero-Knowledge privacy, and on-chain agent auditing on **HashKey Chain**.

🎥 **Demo:** https://youtu.be/QVREoHfyEoE
🌍 **Website:** https://franciscoalmarazlap-cmd.github.io/ANITRAWEBZK.github/

---

## 🚨 The Problem

1. **Money needs internet.** 1.4B people can't transact without connectivity — payment apps fail in rural areas, hospitals, and emergencies.
2. **AI agents have no audit trail.** When an AI executes financial decisions, there is no immutable record of what it did or when.
3. **Proving solvency exposes private data.** Verifying you have funds reveals your entire balance.
4. **No financial discipline tools.** People forget payments and don't save for emergencies.

## ✅ The Solution

| Problem | ANITRAX Solution |
|---|---|
| No internet | Bluetooth P2P transfers + **Offline Smart Queue** with virtual balance |
| AI without audit | Every agent action registered on-chain in **HashKey Chain** |
| Exposed data | **Zero-Knowledge Proofs** — solvency proven, balance hidden |
| Missed payments | **AI-scheduled transfers** with smart reminders and balance checks |
| No savings | **AI-managed emergency fund** with opt-in weekly auto-saving |

---

## ⛓️ HashKey Chain Integration

### Smart Contract: AnitraxRegistry.sol

Deployed on **HashKey Chain Testnet** (Chain ID 133):

```
Contract: 0xe784BF251160506Aa016Dc998218a6f552ca5e73
Deployer: 0x85781C367d8DDaf013CF338bb5c0485ac7c5b160
TX: 0x8276fdf1ec3c38269346c1a91c0fbce1fc3e466ff93991f5c71d550472925c4c
Explorer: https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73
```

> Mainnet deployment in progress (Chain ID 177).

Every AI agent action generates a SHA-256 hash registered on-chain — **zero private user data ever leaves the device**. 9 event types: `task_start`, `agent_execution`, `zk_proof_generated`, `bluetooth_connected`, `transfer_sent`, `transfer_received`, `voice_command_executed`, `critical_event`, `task_end`.

### HSP — Verifiable Settlement Layer

ANITRAX integrates **HSP** (HashKey's official settlement protocol) as its verifiable stablecoin settlement layer on `hashkey-testnet`. See [`anitrax-hsp-payment.ts`](./anitrax-hsp-payment.ts) — a Mandate is signed, settled zero-custody from the user's own wallet, and verified cryptographically by anyone.

---

## 🤖 AI Track — Autonomous Financial Agent (Gemini)

The ANITRAX agent doesn't just chat — it **makes real financial decisions**:

- **Full voice control** in natural language — transfer without touching the screen
- **Agent memory** — remembers frequent contacts and usual amounts: *"You usually send 0.05 to Juan — same amount?"*
- **Autonomous financial analysis** before every transfer: validates balance, pending queue, and behavioral patterns; warns on unusual amounts
- **Multi-step commands**: *"pay Juan half of what I owe him"* — the agent calculates it
- **Voice financial reports**: totals, top contacts, pending transfers
- **Smart payment reminders**: *"On the 20th you have a scheduled payment of 100 but your balance is 50 — you're 50 short"*
- **Every decision audited on HashKey Chain**

## 💰 DeFi Track — Financial Infrastructure

- **Offline Smart Queue** — transfers without internet using virtual balance validation: last known balance minus pending queue; overdrafts are **blocked** even offline
- **Scheduled transfers** — programmed payments (day/hour/recipient) executed by the agent
- **Emergency Fund** — opt-in weekly auto-saving; the user sets the amount, withdraws anytime, and the agent offers it to cover shortfalls: *"You're 50 short but your fund has 80 — use it?"*
- **Tiered yield engine** — 2%–8% monthly based on transfer volume
- **Multi-network**: HashKey Chain, Ethereum Sepolia, Casper Testnet, Polygon Amoy, Base Sepolia
- **HSP settlement** — verifiable stablecoin payments

---

## 📡 Core Features

### Bluetooth P2P — No Internet Required
Direct phone-to-phone transfers via Bluetooth RFCOMM. Works in rural areas, hospitals, emergencies, and mass events.

### Offline Smart Queue
```
Last known balance: 100
Pending #1:  -50  ✅ (virtual balance: 50)
Pending #2:  -50  ✅ (virtual balance: 0)
Pending #3:  -10  ❌ BLOCKED — insufficient virtual balance
```
Auto-syncs to blockchain when connectivity returns.

### Zero-Knowledge Privacy (Circom + snarkjs)
Before every transfer, a ZK solvency proof is generated. The recipient verifies solvency **without ever seeing the balance**. Only `sha256(proof)` leaves the device.

### Contacts with Aliases
Save Bluetooth devices with custom aliases — two contacts with the same device name get distinct aliases ("Juan work" / "Juan neighbor"). Voice selection by alias.

### Accessibility — 3 Modes
| Mode | For | How |
|---|---|---|
| Standard | General use | Full visual UI |
| Synesthetic | Blind users | 100% voice-guided by the agent |
| Visual | Deaf users | No audio, large buttons, max contrast |

Plus 5 colorblind filters.

### Security
BiometricPrompt (fingerprint) · Voice signature · ZK proofs · Bluetooth encryption · On-chain agent audit

---

## 🏗 Architecture

```
User voice command
      ↓
Gemini AI Agent (interprets, analyzes, decides)
      ↓
ZK solvency proof (Circom) → only hash leaves device
      ↓
Bluetooth RFCOMM transfer (offline-capable via Smart Queue)
      ↓
AnitraxRegistry @ HashKey Chain (immutable agent audit)
      ↓
HSP verifiable settlement (stablecoin payments)
```

## 🛠 Tech Stack

- **Android:** Kotlin, XML, BiometricPrompt, Bluetooth RFCOMM, ConnectivityManager
- **AI:** Google Gemini 1.5 Flash, SpeechRecognizer, TTS
- **Blockchain:** Solidity 0.8.19 (HashKey Chain), Odra/Rust (Casper), MetaMask
- **ZK:** Circom, snarkjs, Groth16
- **Settlement:** HSP SDK (TypeScript)
- **Networks:** HashKey Chain (133/177), Ethereum Sepolia, Casper Testnet, Polygon Amoy, Base Sepolia

## 📂 Key Files

| File | Purpose |
|---|---|
| `AnitraxRegistry.sol` | On-chain agent audit contract (HashKey Chain) |
| `anitrax-hsp-payment.ts` | HSP verifiable settlement integration |
| `offline/OfflineQueueManager.kt` | Offline transfer queue + virtual balance |
| `offline/VirtualBalanceCalculator.kt` | Overdraft blocking logic |
| `scheduled/ScheduledTransferManager.kt` | AI-scheduled payments + smart reminders |
| `savings/EmergencyFundManager.kt` | Opt-in emergency fund |
| `ai/OpenAIClient.kt` | Gemini agent: memory, analysis, multi-step commands, voice reports |
| `ui/transfer/TransferActivity.kt` | Transfer flow + offline queue + agent integration |
| `ui/dashboard/DashboardActivity.kt` | Voice reports + contacts + reminders |
| `ui/contacts/ContactsActivity.kt` | Bluetooth contacts with aliases |

## ✅ Status — Fully Functional

- ✅ Running on 2 physical Android devices
- ✅ Real Bluetooth P2P transfers
- ✅ Contract live on HashKey Chain Testnet
- ✅ Offline queue blocking overdrafts
- ✅ AI agent with memory + autonomous analysis
- ✅ ZK proofs before every transfer
- ✅ HSP settlement integration

**ANITRAX is a working application, not a prototype.**

## 👥 Team

- **Francisco Almaraz Ocelo** — Team Lead & Full Stack Developer (app, contracts, ZK, AI, integrations)
- **Edmundo Julian Macias Martinez** — Blockchain Developer (wallet + smart contract support)
- **Oscar Arroyo Pereyda** — UI/UX Designer
- **Jose Carlos Sixto Herrera** — Project Manager
