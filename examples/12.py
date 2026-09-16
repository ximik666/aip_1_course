# Файлы CSV и JSON
import csv
import io
import json
rows = list(csv.DictReader(io.StringIO("name,cents\nчай,120\n")))
assert int(rows[0]["cents"]) == 120
text = json.dumps(rows, ensure_ascii=False)
assert json.loads(text) == rows
