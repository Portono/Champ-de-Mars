from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def data_path(relative_path: str) -> str:
    """Retourne le chemin absolu d'une ressource du dossier data/."""
    return str(DATA_DIR / relative_path)
