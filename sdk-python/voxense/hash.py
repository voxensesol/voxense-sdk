import hashlib
import json
from typing import Any, Dict

def generate_hash(payload: Dict[str, Any]) -> str:
    data = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(data).hexdigest()
