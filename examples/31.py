# Интеграционные тесты и качество проекта
import json
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = Path(folder) / "data.json"
    original = [{"name": "чай", "cents": 120}]
    path.write_text(json.dumps(original, ensure_ascii=False), encoding="utf-8")
    loaded = json.loads(path.read_text(encoding="utf-8"))
    assert loaded == original
    assert sum(r["cents"] for r in loaded) == 120
