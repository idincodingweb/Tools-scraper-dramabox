from dataclasses import dataclass
import os


@dataclass(frozen=True)
class DramaBoxConfig:
    base_url: str = os.getenv("DRAMABOX_BASE_URL", "https://api.dramabox.example")
    app_id: str = os.getenv("DRAMABOX_APP_ID", "dramabox-web")
    app_version: str = os.getenv("DRAMABOX_APP_VERSION", "1.0.0")
    platform: str = os.getenv("DRAMABOX_PLATFORM", "web")
    secret: str = os.getenv("DRAMABOX_SECRET", "change-me")
    timeout: float = float(os.getenv("DRAMABOX_TIMEOUT", "20"))


ENDPOINTS = {
    "search": "/api/v1/drama/search",
    "latest": "/api/v1/drama/latest",
    "detail": "/api/v1/drama/detail",
    "episodes": "/api/v1/drama/episodes",
}
