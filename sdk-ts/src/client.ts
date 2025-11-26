import { Connection, PublicKey } from "@solana/web3.js";

export interface VoxenseClientConfig {
  rpcUrl: string;
  programId: string;
}

export class VoxenseClient {
  private connection: Connection;
  private programId: PublicKey;

  constructor(cfg: VoxenseClientConfig) {
    this.connection = new Connection(cfg.rpcUrl, "confirmed");
    this.programId = new PublicKey(cfg.programId);
  }

  async submitProof(hash: string, sensorType: string = "multi") {
    // TODO: build and send Solana tx to voxense-core
    return {
      status: "mock",
      hash,
      sensorType,
      programId: this.programId.toBase58()
    };
  }
}
