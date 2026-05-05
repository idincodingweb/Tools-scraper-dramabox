from __future__ import annotations

import secrets
import time
from typing import Any

import httpx

from .config import DramaBoxConfig, ENDPOINTS
from .signing import sign_payload


class DramaBoxClient:
    def __init__(self, config: DramaBoxConfig | None = None):
        self.config = config or DramaBoxConfig()
        self._client = httpx.Client(
            base_url=self.config.base_url,
            timeout=self.config.timeout,
            headers={
                "User-Agent": f"DramaBoxTool/{self.config.app_version}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-App-Id": self.config.app_id,
                "X-App-Version": self.config.app_version,
                "X-Platform": self.config.platform,
            },
        )

    def close(self) -> None:
        self._client.close()

    def _signed_post(self, endpoint_key: str, payload: dict[str, Any]) -> dict[str, Any]:
        ts = str(int(time.time()))
        nonce = secrets.token_hex(8)
        signature = sign_payload(self.config.secret, ts, nonce, payload)

        headers = {
            "X-Timestamp": ts,
            "X-Nonce": nonce,
            "X-Signature": signature,
        }

        res = self._client.post(ENDPOINTS[endpoint_key], json=payload, headers=headers)
        res.raise_for_status()
        return res.json()

    def search(self, keyword: str, page: int = 1, size: int = 20) -> dict[str, Any]:
        return self._signed_post("search", {"keyword": keyword, "page": page, "size": size})

    def latest(self, page: int = 1, size: int = 20) -> dict[str, Any]:
        return self._signed_post("latest", {"page": page, "size": size})

    def detail(self, drama_id: str) -> dict[str, Any]:
        return self._signed_post("detail", {"drama_id": drama_id})

    def episodes(self, drama_id: str, page: int = 1, size: int = 100) -> dict[str, Any]:
        return self._signed_post(
            "episodes",
            {"drama_id": drama_id, "page": page, "size": size},
        )
