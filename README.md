<p align="center">
  <img src="https://i.imgur.com/NWptykH.png" width="100%" alt="VOXENSE Banner"/>
</p>

<h1 align="center">🛰️ VOXENSE CORE</h1>
<p align="center">
  <b>The Proof-of-Sensing Protocol</b><br/>
  <i>Core smart contracts powering the Real-World Sensor Network on Solana.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/voxensesol/voxense-core?style=flat-square"/>
  <img src="https://img.shields.io/badge/Network-Solana-9945FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/DePIN-Enabled-C0FF00?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Beta-green?style=flat-square"/>
</p>

## Overview
VOXENSE Core is the foundational layer of the VOXENSE Network — a Spatial DePIN protocol that verifies real-world sensing through on-chain cryptographic proof (GPS, Audio, Ambient, Motion). Nodes submit hashes, PoS validates, rewards are issued in `$VOX`.

> When the environment agrees, the network believes.

## Core Modules
- **PoS Engine** — validate multi-sensor data between nodes  
- **Reward Distributor** — issue `$VOX` to verified contributors  
- **Node Registry** — register device fingerprints & activity  
- **Spatial Ledger** — immutable proofs of sensing events  
- **Reputation System** — node trust scoring

## Architecture
[Sensors] -> [Voxense SDK] -> [PoS Engine] -> [Solana Contracts] -> [Reality Layer / Marketplace]

scss
Salin kode

## Token Utility — $VOX
Submit Hash • Verified Consensus • Uptime • Data Access Fees.

## Example (stub)
```rust
// minimal stub; real PoS extends from here
pub fn submit_proof(ctx: Context<SubmitProof>, data_hash: [u8; 32]) -> Result<()> { /* ... */ Ok(()) }
Dev Setup
Rust, Solana CLI, Anchor

bash
Salin kode
git clone https://github.com/voxensesol/voxense-core.git
cd voxense-core
anchor build && anchor test
