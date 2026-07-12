# 🟣 ANITRAX — Agentic Financial System on HashKey Chain

> **ANITRAX is the first mobile peer-to-peer financial system where an autonomous AI agent manages, executes, schedules, and audits money movements — with every single agent decision immutably registered on HashKey Chain.** It works without internet, protects user privacy with Zero-Knowledge Proofs, and builds financial discipline through AI-scheduled payments and an AI-managed emergency fund.

**HashKey Chain On-Chain Horizon Hackathon 2026 — AI & DeFi Tracks**

[![HashKey](https://img.shields.io/badge/HashKey_Chain-Testnet-purple)](https://testnet-explorer.hsk.xyz)
[![Android](https://img.shields.io/badge/Android-Kotlin-green?logo=android)](https://developer.android.com)
[![AI](https://img.shields.io/badge/AI-Gemini_1.5-orange?logo=google)](https://ai.google.dev)
[![ZK](https://img.shields.io/badge/Zero--Knowledge-Groth16-blueviolet)](#)
[![HSP](https://img.shields.io/badge/HSP-Verifiable_Settlement-blue)](https://hsp-hackathon.hashkeymerchant.com/docs)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🌐 Links

| Resource | URL |
|---|---|
| 🌍 Website | https://franciscoalmarazlap-cmd.github.io/ANITRAXWEBHashKey-Chain/ |
| 🟣 Live Contract on HashKey Chain Testnet | https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73 |
| 🎥 YouTube Demo | https://youtu.be/QVREoHfyEoE?si=psbOALnukDiSzVUP |
| 🔗 Repository |https://github.com/franciscoalmarazlap-cmd/ANITRAXWEBHashKey-Chain|

---

## ❌ The Problem

Digital money today fails in four fundamental ways — and no existing system solves them together:

**1. Money needs internet to move.**
Over 1.4 billion people live or work in places where connectivity fails: rural communities, hospitals with restricted networks, mass events with saturated antennas, disaster zones. When the connection dies, every banking and crypto app on the planet becomes a brick. Money that cannot move when you need it most is not really yours.

**2. AI agents operate financially with zero accountability.**
The industry is racing to let AI agents execute payments, manage balances, and make financial decisions — but there is no immutable, independently verifiable record of what an agent did, when it did it, or whether it acted within its mandate. Users are asked to blindly trust a black box with their money. This is the single biggest unsolved problem of agentic finance.

**3. Proving solvency means exposing everything.**
To demonstrate you can afford a payment, traditional systems reveal your full balance and transaction history. Financial privacy and financial verification are treated as opposites — when cryptography proved years ago they don't have to be.

**4. Financial discipline has no infrastructure.**
People forget recurring payments, discover too late that their balance won't cover an obligation, and have no frictionless mechanism to build emergency savings. Banks solved this with expensive human infrastructure; crypto never solved it at all.

## ✅ The ANITRAX Answer

| Problem | ANITRAX Solution |
|---|---|
| No internet | **Bluetooth P2P transfers** + **Offline Smart Queue** with virtual-balance overdraft protection |
| Unaccountable AI | **Every agent action hashed and registered on HashKey Chain** — a public, immutable audit trail |
| Exposed balances | **Zero-Knowledge solvency proofs** — the recipient learns you *can* pay, never *how much* you have |
| No discipline | **AI-scheduled payments** with proactive balance-aware reminders + **opt-in AI-managed emergency fund** |

---

## 🟣 HashKey Chain — The Agentic Audit Layer

ANITRAX treats HashKey Chain as the **source of truth for AI accountability**. Every meaningful decision the agent makes — starting a task, generating a ZK proof, executing a transfer, detecting an error — produces a SHA-256 fingerprint that is automatically registered on-chain, without any user intervention.

The result: **anyone can independently verify what the ANITRAX agent did and when, while learning absolutely nothing private about the user.** This is what responsible agentic finance looks like.

### Smart Contract: AnitraxRegistry.sol (Solidity 0.8.19)

**Deployed and live on HashKey Chain Testnet:**

```
Contract:  0xe784BF251160506Aa016Dc998218a6f552ca5e73
Deployer:  0x85781C367d8DDaf013CF338bb5c0485ac7c5b160
TX:        0x8276fdf1ec3c38269346c1a91c0fbce1fc3e466ff93991f5c71d550472925c4c
Chain ID:  133 (testnet) — mainnet deployment (Chain ID 177) in progress
Explorer:  https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73
```

```solidity
contract AnitraxRegistry {
    struct Event {
        string eventId;
        string eventType;
        string eventHash;   // SHA-256 fingerprint — never private data
        uint256 timestamp;
        address sender;
    }

    event EventRegistered(string eventId, string eventType, string eventHash,
                          uint256 timestamp, address indexed sender);

    function registerEvent(string memory eventId, string memory eventType,
                           string memory eventHash) public;
    function getEventCount() public view returns (uint256);
    function getEvent(uint256 index) public view returns (...);
}
```

The contract stores only cryptographic fingerprints. **No names, no balances, no amounts, no contacts — ever.** Privacy by architecture, not by promise.

### 9 agent events that generate real on-chain transactions:

| Event | When the agent registers it |
|---|---|
| `task_start` | A transfer session begins |
| `agent_execution` | The agent executes an autonomous action |
| `zk_proof_generated` | A ZK solvency proof is created and verified |
| `bluetooth_connected` | A P2P device connection is established |
| `transfer_sent` | A transfer completes successfully |
| `transfer_received` | An incoming transfer is confirmed |
| `voice_command_executed` | A natural-language command is processed |
| `critical_event` | The agent detects and logs a system error |
| `task_end` | The agent closes the task |

### HSP Integration — Verifiable Settlement Layer

ANITRAX integrates **HSP, HashKey's official settlement protocol**, as its verifiable stablecoin settlement layer on `hashkey-testnet` (see [`anitrax-hsp-payment.ts`](./anitrax-hsp-payment.ts)):

1. ANITRAX signs an **EIP-712 Mandate** — a cryptographic payment intent
2. The user's **own wallet** settles on-chain — HSP is **zero-custody**, no service ever touches the funds
3. The Coordinator observes the settlement and emits a signed **Receipt**
4. Any third party can re-run the verification independently: `requiredCapabilities ⊆ satisfiedCapabilities` ⇒ ACCEPT

This combination — HSP for verifiable settlement + AnitraxRegistry for agent audit — makes ANITRAX payments **trustless on both ends**: the money movement is provable, and the AI that moved it is accountable.

---

## 🤖 AI Track — A Truly Autonomous Financial Agent

Most "AI-powered" finance apps use AI as a chatbot skin. The ANITRAX agent (Google Gemini 1.5) **owns the entire financial workflow** — it listens, decides, warns, executes, schedules, saves, and reports. And every one of those verbs leaves an immutable trace on HashKey Chain.

### 🎤 Voice-first execution
The user speaks in natural language; the agent interprets the financial intent, selects the correct wallet and network, generates the ZK proof, executes the Bluetooth transfer, and confirms the result by voice. **The user never needs to touch the screen** — which is also what makes ANITRAX fully usable by blind users.

### 🧠 Persistent agent memory
The agent remembers who you pay, how much, and how often — across sessions. Open a transfer to a frequent contact and it proactively suggests: *"You usually send 0.05 to Juan — same amount?"* Memory is stored locally on-device; only hashes ever leave it.

### 🔍 Autonomous pre-transfer analysis
Before any money moves, the agent independently evaluates: real current balance, total pending in the offline queue, and the user's historical pattern with that contact. It confirms reasonable transfers, **warns** when an amount is unusually large, and **blocks** transfers that are mathematically impossible — explaining its reasoning out loud.

### 🧮 Multi-step command resolution
*"Pay Juan half of what I owe him."* The agent retrieves the debt from transfer history, computes the amount, validates solvency, and asks for a single confirmation. Complex financial intent, one sentence.

### 📅 Proactive payment intelligence
The agent doesn't wait to be asked. Days before a scheduled payment it cross-checks your balance and speaks up: *"On the 20th you have a scheduled payment of 100, but your balance is 50 — you're 50 short."* If the emergency fund can cover the gap, it offers that too.

### 📊 Voice financial reports
Double-tap your balance (or just say "report") and the agent narrates a natural-language summary: totals sent and received, most frequent contacts, pending offline transfers, fund status.

### ⛓ Radical accountability
Every capability above emits events to **AnitraxRegistry on HashKey Chain**. The agent is powerful *because* it is auditable — not in spite of it.

---

## 💰 DeFi Track — New Financial Infrastructure

### 📡 Offline Smart Queue — the overdraft-proof offline wallet

When connectivity drops, ANITRAX switches to its last verified balance and lets the user keep transacting — with hard mathematical guarantees:

```
Last known balance: 100
Pending #1:  -50   ✅  (virtual balance: 50)
Pending #2:  -50   ✅  (virtual balance: 0)
Pending #3:  -10   ❌  BLOCKED — insufficient virtual balance
```

The virtual balance = last verified balance − everything already queued. **Overspending is impossible even with zero connectivity.** The moment internet returns, the queue syncs automatically to the blockchain and the agent reports the result.

### 📅 AI-Scheduled Transfers

Program a payment once — recipient, amount, day of the month, hour — and the agent takes over: it tracks the due date, verifies your balance days in advance, reminds you with specifics (not generic notifications), and offers one-tap or one-word execution when the date arrives. Recurring obligations stop depending on human memory.

### 🏦 AI-Managed Emergency Fund — savings with consent

- **Strictly opt-in**: nothing is deducted unless the user explicitly activates it and chooses the weekly amount
- The agent sets aside that amount every week; if the balance is too low, it **skips and notifies** instead of overdrafting
- The user withdraws **any amount, any time** — it's their money, frictionless
- Integrated with payments: when an obligation exceeds the balance, the agent offers the fund — *"You're 50 short but your fund has 80. Want me to cover it?"*
- Full history of every contribution, skip, and withdrawal

### 📈 Tiered Yield Engine

Rewards scale with transfer volume, simulating a liquidity-incentive protocol (architecture ready for real DeFi protocol integration):

| Tier | Monthly Volume | Yield |
|---|---|---|
| 🥉 Starter | 0 – 0.1 ETH | 2% monthly |
| 🥈 Explorer | 0.1 – 0.5 ETH | 3% monthly |
| 🥇 Builder | 0.5 – 2 ETH | 5% monthly |
| 💎 Validator | 2 – 5 ETH | 6% monthly |
| 🐋 Whale | 5+ ETH | 8% monthly |

### 🌐 Multi-network by design

Users add wallets once and choose the rail per transfer, with live balances:

| Network | Symbol | Status |
|---|---|---|
| **HashKey Chain** | **HSK** | ✅ **Active — agentic audit + HSP settlement** |
| Ethereum Sepolia | ETH | ✅ Active |
| Casper Testnet | CSPR | ✅ Active |
| Polygon Amoy | MATIC | ✅ Ready |
| Base Sepolia | ETH | ✅ Ready |

---

## 🔐 Zero-Knowledge Proofs — Verification Without Exposure

Before every transfer, the agent generates a Groth16 solvency proof from a Circom circuit:

```
User's real balance:  0.05 ETH   ← never leaves the device
Transfer amount:      0.001 ETH  ← public
What is transmitted:  sha256(proof) — a fingerprint, nothing more
```

The recipient gains cryptographic certainty that the sender is solvent while learning **nothing** about their actual holdings. The proof hash is then registered on HashKey Chain — so even the *privacy layer* is auditable.

**What ZK protects in ANITRAX:**
- **🔒 Identity** — validity proven without names, credentials, or biometrics
- **💰 Funds** — solvency without balances or history
- **🤖 Agent inputs** — what you tell your agent stays on your device
- **🟣 On-chain integrity** — every proof fingerprinted on HashKey Chain

---

## 📡 Bluetooth P2P — Where Every Other Wallet Dies

ANITRAX moves money phone-to-phone over Bluetooth RFCOMM — no WiFi, no mobile data, no intermediary server, no mesh dependency. The transfer payload carries the ZK solvency hash, so even offline recipients get cryptographic assurance.

**Built for the real world:** rural communities without coverage · hospitals with locked-down networks · stadiums and festivals with saturated antennas · natural disasters · any country with fragile infrastructure.

## 👥 Contacts with Aliases

Bluetooth device names are chaos — ANITRAX fixes it. Save any device with a custom alias; two phones broadcasting the same name get distinct identities ("Juan work" / "Juan neighbor"). Saved contacts appear instantly with ⭐ before any scan, aliases travel through the entire transfer flow, and voice selection resolves by alias.

## ♿ Accessibility — Finance for Every Body

| Mode | Designed for | Experience |
|---|---|---|
| **Standard** | General use | Full visual UI + multi-network selector |
| **Synesthetic** | Blind and low-vision users | 100% voice-guided — the agent narrates and listens at every step |
| **Visual** | Deaf and hard-of-hearing users | Zero audio dependency, large targets, maximum contrast |

All modes include 5 colorblind filters. **Access to money should never depend on your abilities** — and because the agent already runs everything by voice, accessibility in ANITRAX is native, not an afterthought.

## 🔐 Multi-layer Security

| Layer | Function |
|---|---|
| BiometricPrompt | Fingerprint authentication before sensitive actions |
| Voice Authentication | The user's unique voice signature |
| ZK Proofs (Circom/Groth16) | Cryptographic privacy of funds |
| Bluetooth Encryption | P2P channel protection |
| **HashKey Chain** | **Immutable agent audit + HSP verifiable settlement** |
| Ethereum Sepolia / Casper | Cross-chain transaction registry |

---

## ⚙️ System Architecture

```
┌────────────────────────────────────────────────────────┐
│                   ANITRAX Android App                   │
│                                                         │
│    🎤 Voice ──→ 🤖 Gemini Agent ──→ 📡 Bluetooth P2P    │
│                     │                                   │
│      ┌──────────────┼──────────────┐                    │
│      ↓              ↓              ↓                    │
│  🧠 Memory    🔐 ZK Proofs    📡 Offline Queue          │
│      ↓              ↓              ↓                    │
│  📅 Scheduler  🏦 Emergency   💱 Multi-network          │
│                   Fund                                  │
│                     │                                   │
│                     ↓                                   │
│      AnitraxRegistry @ HashKey Chain (Chain ID 133)     │
│              — agentic audit layer —                    │
│                     ↓                                   │
│      HSP Verifiable Settlement (stablecoins, USDC)      │
└────────────────────────────────────────────────────────┘
```

## 📂 Key Files

| File | Purpose |
|---|---|
| `AnitraxRegistry.sol` | On-chain agent audit contract (HashKey Chain) |
| `anitrax-hsp-payment.ts` | HSP verifiable settlement integration |
| `offline/OfflineQueueManager.kt` | Offline queue, virtual balance, sync engine |
| `offline/VirtualBalanceCalculator.kt` | Overdraft-blocking validation + agent messaging |
| `scheduled/ScheduledTransferManager.kt` | Scheduled payments + balance-aware smart reminders |
| `savings/EmergencyFundManager.kt` | Opt-in weekly auto-saving + shortfall coverage |
| `ai/OpenAIClient.kt` | Gemini agent: memory, autonomous analysis, multi-step commands, voice reports |
| `ui/transfer/TransferActivity.kt` | Transfer flow with offline queue + agent integration |
| `ui/dashboard/DashboardActivity.kt` | Voice reports, reminders, saved contacts |
| `ui/contacts/ContactsActivity.kt` | Bluetooth contact discovery with alias system |

## 🛠 Tech Stack

**Android:** Kotlin, XML, BiometricPrompt, Bluetooth RFCOMM, ConnectivityManager
**AI:** Google Gemini 1.5 Flash, SpeechRecognizer, Text-to-Speech
**Blockchain:** Solidity 0.8.19 (HashKey Chain), Odra/Rust (Casper), MetaMask, Remix
**ZK:** Circom, snarkjs, Groth16
**Settlement:** HSP SDK (TypeScript, EIP-712 mandates, zero-custody)

## 🧪 Try it in 60 Seconds

1. Open ANITRAX on **2 phones** with Bluetooth enabled
2. Pick a contact (or save one with an alias) → enter an amount
3. Tap **Send** → the agent analyzes your balance, pending queue, and history — out loud
4. Confirm by voice or fingerprint → transfer flies over Bluetooth
5. **Turn off internet and try again** — watch the Offline Smart Queue accept valid transfers and block overdrafts
6. Say **"report"** — hear your financial summary
7. Verify the agent's audit trail on [testnet-explorer.hsk.xyz](https://testnet-explorer.hsk.xyz/address/0xe784BF251160506Aa016Dc998218a6f552ca5e73)

## ✅ Status — Fully Functional, Not a Prototype

- ✅ Running on 2 physical Android devices
- ✅ Real Bluetooth P2P transfers completed
- ✅ `AnitraxRegistry` live on **HashKey Chain Testnet** — mainnet in progress
- ✅ HSP verifiable settlement integrated
- ✅ Offline Smart Queue blocking overdrafts with zero connectivity
- ✅ AI agent: memory, autonomous analysis, multi-step commands, scheduled payments, emergency fund, voice reports
- ✅ ZK solvency proofs before every transfer
- ✅ 3 accessibility modes + 5 colorblind filters

## 👤 Author

**Francisco Almaraz Ocelo** — sole developer of ANITRAX.

Designed and built the entire system end to end: the Android application (Kotlin), the autonomous AI agent and all its capabilities (memory, financial analysis, multi-step commands, scheduling, emergency fund, voice reports), the smart contracts on HashKey Chain (Solidity) and Casper (Odra/Rust), the Zero-Knowledge proof system (Circom/snarkjs), the Bluetooth P2P transfer layer, the Offline Smart Queue, the HSP settlement integration, the accessibility modes, and the on-chain agent audit architecture.


## ⚠️ Notes

- Test networks only — do not use with real tokens
- Mainnet deployment (Chain ID 177) in progress

## 📄 License

MIT License — Copyright (c) 2026 Francisco Almaraz Ocelo
Built for the HashKey Chain On-Chain Horizon Hackathon 2026.
