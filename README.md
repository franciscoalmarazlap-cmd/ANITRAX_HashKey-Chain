# 🟣 ANITRAX — Agentic Financial System on HashKey Chain

> **ANITRAX is the first mobile peer-to-peer financial transfer system that uses HashKey Chain as its agentic audit layer** — combining offline Bluetooth transfers, an autonomous AI agent with memory, Zero-Knowledge Proofs, AI-scheduled payments, an AI-managed emergency fund, and automatic on-chain registration of every agent action.

**HashKey Chain On-Chain Horizon Hackathon 2026 — AI & DeFi Tracks**

[![HashKey](https://img.shields.io/badge/HashKey_Chain-Testnet-purple)](https://testnet-explorer.hsk.xyz)
[![Android](https://img.shields.io/badge/Android-Kotlin-green?logo=android)](https://developer.android.com)
[![AI](https://img.shields.io/badge/AI-Gemini-orange?logo=google)](https://ai.google.dev)
[![ZK](https://img.shields.io/badge/Zero--Knowledge-Privacy-blueviolet)](#)
[![HSP](https://img.shields.io/badge/HSP-Settlement-blue)](https://hsp-hackathon.hashkeymerchant.com/docs)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🌐 Links

| Resource | URL |
|---|---|
| 🌍 Website | https://franciscoalmarazlap-cmd.github.io/ANITRAWEBZK.github/ |
| 🟣 Contract on HashKey Chain Testnet | https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73 |
| 🎥 YouTube Demo | https://youtu.be/QVREoHfyEoE |
| 🔗 Repository | https://github.com/franciscoalmarazlap-cmd/ANITRAXGASPER |

---

## ❌ The Problem ANITRAX Solves

Digital money has 4 fundamental problems nobody has solved together:

**1. It needs internet to move**
Millions of people in rural areas, hospitals, mass events, or emergencies can't transfer because they have no signal. Traditional banking apps simply don't work offline.

**2. AI agents have no audit trail**
When an AI makes financial decisions on behalf of the user (executing transfers, verifying balances, confirming amounts), nobody can verify what the agent did, when, or whether it acted correctly. There is no immutable record of agent actions.

**3. Transfers expose private data**
To verify someone has enough balance, traditional systems expose the full balance. There is no way to prove "I have enough" without showing how much you have.

**4. No financial discipline infrastructure**
People forget scheduled payments and have no frictionless way to build emergency savings.

## ✅ ANITRAX solves all 4 simultaneously:

| Problem | ANITRAX Solution |
|---|---|
| No internet | Bluetooth P2P + **Offline Smart Queue** with virtual balance validation |
| AI without audit | Every agent action registered on-chain in **HashKey Chain** |
| Exposed data | Zero-Knowledge Proofs — solvency proven, never the real balance |
| No discipline | **AI-scheduled payments** with smart reminders + **AI-managed emergency fund** |

---

## 🟣 HashKey Chain — The Agentic Core of ANITRAX

ANITRAX uses HashKey Chain as the **immutable audit layer of the AI agent**. Every time the agent makes an important decision, the cryptographic hash of that action is registered on-chain — automatically, without user intervention.

### Smart Contract: AnitraxRegistry.sol (Solidity 0.8.19)

**Deployed and live on HashKey Chain Testnet:**

```
Contract:  0xe784BF251160506Aa016Dc998218a6f552ca5e73
Deployer:  0x85781C367d8DDaf013CF338bb5c0485ac7c5b160
TX:        0x8276fdf1ec3c38269346c1a91c0fbce1fc3e466ff93991f5c71d550472925c4c
Chain ID:  133 (testnet) — mainnet deployment (177) in progress
Explorer:  https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73
```

```solidity
contract AnitraxRegistry {
    struct Event {
        string eventId;
        string eventType;
        string eventHash;   // SHA-256 — never private data
        uint256 timestamp;
        address sender;
    }

    function registerEvent(string memory eventId, string memory eventType, string memory eventHash) public;
    function getEventCount() public view returns (uint256);
    function getEvent(uint256 index) public view returns (...);
}
```

The contract receives the SHA-256 hash of each agent event and registers it on-chain. **It never stores private user data** — only verifiable cryptographic fingerprints.

### Events that generate real HashKey Chain transactions:

| Event | When it occurs |
|---|---|
| `task_start` | Agent starts a transfer session |
| `agent_execution` | AI agent executes an autonomous action |
| `zk_proof_generated` | ZK solvency proof generated |
| `bluetooth_connected` | Bluetooth connection established |
| `transfer_sent` | Transfer completed successfully |
| `transfer_received` | Transfer received |
| `voice_command_executed` | Voice command processed by the agent |
| `critical_event` | Agent detects a critical error |
| `task_end` | Agent completes the task |

### HSP — Verifiable Settlement Layer (official HashKey framework)

ANITRAX integrates **HSP** as its verifiable stablecoin settlement layer on `hashkey-testnet`. See [`anitrax-hsp-payment.ts`](./anitrax-hsp-payment.ts):

1. ANITRAX signs a **Mandate** (EIP-712 payment intent)
2. The user's own wallet settles on-chain (**zero-custody**)
3. The Coordinator observes and emits a signed **Receipt**
4. Anyone can cryptographically re-verify the payment — trustless

---

## 🤖 AI Track — Truly Autonomous Financial Agent (Gemini)

The ANITRAX agent is not decorative AI — it **makes real autonomous financial decisions**:

### Voice-first control
- Listens to natural language commands, interprets financial intent
- Selects the correct wallet and network, generates ZK proof, executes the Bluetooth transfer, confirms by voice — **without the user touching the screen**

### Agent memory
- Remembers frequent contacts and usual amounts: *"You usually send 0.05 to Juan — same amount?"*
- Learns user patterns across sessions

### Autonomous financial analysis
- Before every transfer: validates real balance, pending offline queue, and behavioral patterns
- Warns on unusual amounts, blocks impossible ones

### Multi-step commands
- *"Pay Juan half of what I owe him"* — the agent calculates from history and executes

### Smart payment reminders
- *"On the 20th you have a scheduled payment of 100, but your balance is 50 — you're 50 short."*
- Checks balance against every upcoming payment, days in advance

### Voice financial reports
- Totals sent/received, top contacts, pending queue — narrated naturally

### Every decision audited on-chain
- All of the above generates immutable events in **HashKey Chain**

---

## 💰 DeFi Track — New Financial Infrastructure

### 📡 Offline Smart Queue — money without internet
```
Last known balance: 100
Pending #1:  -50  ✅ (virtual balance: 50)
Pending #2:  -50  ✅ (virtual balance: 0)
Pending #3:  -10  ❌ BLOCKED — insufficient virtual balance
```
Transfers created offline use the last known balance minus pending queue. **Overdrafts are blocked even offline.** Auto-syncs to blockchain when connectivity returns.

### 📅 AI-Scheduled Transfers
The user programs: recipient, amount, day and hour (e.g., pay the card on the 20th). The agent reminds days in advance, validates the balance, and offers to execute when due.

### 🏦 AI-Managed Emergency Fund (opt-in)
- Only activates if the user explicitly accepts; the user sets the weekly amount
- The agent sets aside that amount weekly; if balance is low, it notifies and skips
- Withdraw anytime — savings, covering pending payments, or completing transfers
- If a payment falls short: *"You're 50 short but your fund has 80 — want to use it?"*

### 📈 Tiered Yield Engine

| Tier | Monthly Volume | Yield |
|---|---|---|
| 🥉 Starter | 0 – 0.1 ETH | 2% |
| 🥈 Explorer | 0.1 – 0.5 ETH | 3% |
| 🥇 Builder | 0.5 – 2 ETH | 5% |
| 💎 Validator | 2 – 5 ETH | 6% |
| 🐋 Whale | 5+ ETH | 8% |

### 🌐 Multi-network without friction

| Network | Symbol | Status |
|---|---|---|
| **HashKey Chain** | **HSK** | ✅ **Active — agentic audit layer** |
| Ethereum Sepolia | ETH | ✅ Active |
| Casper Testnet | CSPR | ✅ Active |
| Polygon Amoy | MATIC | ✅ Ready |
| Base Sepolia | ETH | ✅ Ready |

---

## 🔐 Zero-Knowledge Proofs — Total Privacy

Before every Bluetooth transfer, the AI agent generates a ZK solvency proof using a Circom circuit:

```
User's real balance: 0.05 ETH  ← never transmitted
Transfer amount:     0.001 ETH ← public
ZK proof generated:  sha256(proof) ← only this leaves the device
```

The recipient verifies the sender has sufficient funds **without knowing exactly how much they have**. The ZK proof hash is also registered on HashKey Chain.

**🔒 Private identity** — user proves validity without revealing name, credentials, or biometrics
**💰 Hidden funds** — solvency verified without exposing balance or history
**🤖 Private agent actions** — user inputs to the AI never exposed publicly
**🟣 ZK + HashKey** — every ZK proof hash registered on-chain — verifiable, immutable, zero sensitive data

---

## 📡 Bluetooth P2P — No internet, no limits

ANITRAX transfers money phone-to-phone via Bluetooth RFCOMM — no WiFi, no mobile data, no intermediary server.

**Real use cases:** rural areas without signal · hospitals with restricted networks · mass events with saturated networks · emergencies where internet fails · countries with limited infrastructure

The transfer payload includes the **ZK hash** as proof of solvency.

## 👥 Contacts with Aliases

Save Bluetooth devices with custom aliases — two contacts with the same device name get distinct aliases ("Juan work" / "Juan neighbor"). Saved contacts appear first (⭐) without scanning. Voice selection works by alias.

## ♿ Accessibility — 3 modes for everyone

| Mode | For whom | How it works |
|---|---|---|
| **Standard** | General use | Full visual UI + multi-network selector |
| **Synesthetic** | Visual impairment | 100% voice — the agent guides every step |
| **Visual** | Hearing impairment | No audio, large buttons, max contrast |

All 3 modes include 5 colorblind filters. Access to money shouldn't depend on your abilities.

## 🔐 Multi-layer Security

| Technology | Function |
|---|---|
| BiometricPrompt | Fingerprint authentication |
| Voice Authentication | Unique voice signature |
| ZK Proofs (Circom) | Cryptographic privacy of funds |
| Bluetooth Encryption | P2P data protection |
| **HashKey Chain** | **Immutable AI agent audit + HSP settlement** |
| Ethereum Sepolia / Casper | Cross-chain transaction registry |

---

## ⚙️ System Architecture

```
┌──────────────────────────────────────────────────────┐
│                  ANITRAX Android App                  │
│                                                       │
│   🎤 Voice → 🤖 Gemini Agent → 📡 Bluetooth P2P       │
│        ↓            ↓                                 │
│   🧠 Memory   🔐 ZK Proof (Circom/snarkjs)            │
│        ↓            ↓                                 │
│   📅 Scheduler  🏦 Emergency Fund  📡 Offline Queue   │
│                     ↓                                 │
│        AnitraxRegistry @ HashKey Chain                │
│              (agentic audit layer)                    │
│                     ↓                                 │
│        HSP Verifiable Settlement (stablecoins)        │
└──────────────────────────────────────────────────────┘
```

## 📂 Key Files

| File | Purpose |
|---|---|
| `AnitraxRegistry.sol` | On-chain agent audit contract (HashKey Chain) |
| `anitrax-hsp-payment.ts` | HSP verifiable settlement integration |
| `offline/OfflineQueueManager.kt` | Offline queue + virtual balance |
| `offline/VirtualBalanceCalculator.kt` | Overdraft blocking logic |
| `scheduled/ScheduledTransferManager.kt` | AI-scheduled payments + smart reminders |
| `savings/EmergencyFundManager.kt` | Opt-in AI-managed emergency fund |
| `ai/OpenAIClient.kt` | Gemini agent: memory, analysis, multi-step, voice reports |
| `ui/transfer/TransferActivity.kt` | Transfer flow + offline + agent |
| `ui/dashboard/DashboardActivity.kt` | Voice reports + reminders + contacts |
| `ui/contacts/ContactsActivity.kt` | Bluetooth contacts with aliases |

## 🛠 Tech Stack

**Android:** Kotlin, XML, BiometricPrompt, Bluetooth RFCOMM, ConnectivityManager
**AI:** Google Gemini 1.5 Flash, SpeechRecognizer, TTS
**Blockchain:** Solidity 0.8.19 (HashKey Chain), Odra/Rust (Casper), MetaMask
**ZK:** Circom, snarkjs, Groth16
**Settlement:** HSP SDK (TypeScript)

## 🧪 Try it in 60 seconds

1. Open ANITRAX on **2 phones** with Bluetooth on
2. Select a contact → enter amount (e.g. `0.1`)
3. Tap **Send** → the agent analyzes your balance and history
4. Confirm by voice or fingerprint
5. Turn off internet and try again — watch the **Offline Smart Queue** block overdrafts
6. Verify agent events on [testnet-explorer.hsk.xyz](https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73)

## ✅ Status — Fully Functional

- ✅ Running on 2 physical Android devices
- ✅ Real Bluetooth P2P transfers completed
- ✅ Contract live on **HashKey Chain Testnet**
- ✅ HSP settlement integration
- ✅ Offline queue blocking overdrafts
- ✅ AI agent with memory + autonomous analysis + scheduled payments + emergency fund
- ✅ ZK proofs before every transfer

**ANITRAX is a working application, not a prototype.**

## 👥 Team

- **Francisco Almaraz Ocelo** — Team Lead & Full Stack Developer (app, smart contracts, ZK, AI, integrations)
- **Edmundo Julian Macias Martinez** — Blockchain Developer (wallet + smart contract support)
- **Oscar Arroyo Pereyda** — UI/UX Designer
- **Jose Carlos Sixto Herrera** — Project Manager

## ⚠️ Notes

- Test networks only — do not use with real tokens
- Mainnet deployment (Chain ID 177) in progress

## 📄 License

MIT License — Copyright (c) 2026 Francisco Almaraz Ocelo
Built for the HashKey Chain On-Chain Horizon Hackathon 2026.
