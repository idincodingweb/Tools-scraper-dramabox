import hashlib
import hmac
import json
from typing import Any


def stable_json(data: Any) -> str:
    return json.dumps(data, separators=(",", ":"), sort_keys=True, ensure_ascii=False)


def sign_payload(secret: str, timestamp: str, nonce: str, payload: dict) -> str:
    msg = f"{timestamp}.{nonce}.{stable_json(payload)}".encode("utf-8")
    key = secret.encode("utf-8")
    return hmac.new(key, msg, hashlib.sha256).hexdigest()
