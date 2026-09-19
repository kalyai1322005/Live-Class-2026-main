from pathlib import Path
import sys


PROJECT_DIR = (
    Path(__file__).resolve().parents[1]
    / "Complete MCP"
    / "TimeTrackProject"
    / "timetrack"
)
sys.path.insert(0, str(PROJECT_DIR))

from main import app  # noqa: E402

__all__ = ["app"]
