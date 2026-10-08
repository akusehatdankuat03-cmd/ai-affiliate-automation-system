from pathlib import Path
from urllib.request import urlretrieve


class MediaService:
    def download_asset(self, url: str, target_dir: str = "media") -> dict:
        path = Path(target_dir)
        path.mkdir(exist_ok=True, parents=True)
        filename = url.split("/")[-1] or "downloaded_asset"
        dest = path / filename

        try:
            urlretrieve(url, str(dest))
            return {"status": "downloaded", "path": str(dest), "url": url}
        except Exception as exc:
            return {"status": "failed", "error": str(exc), "url": url}
