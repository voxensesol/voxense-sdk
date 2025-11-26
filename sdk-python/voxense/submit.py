from typing import Dict

def submit_proof(data_hash: str, sensor_type: str = "multi") -> Dict:
    """
    Placeholder submit. Later this will build and send
    a Solana transaction to voxense-core.
    """
    return {
        "status": "queued",
        "hash": data_hash,
        "sensor_type": sensor_type,
    }
