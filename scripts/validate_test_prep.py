"""Validate public multi-exam Test Prep sample catalogs (no dependencies)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    manifest = read("test-prep.json")
    assert manifest["schema_version"] == 1 and manifest["id"] == "test-prep"
    assert [t["id"] for t in manifest["tracks"]] == ["tsi-math", "asvab", "sat", "act"]
    assert read("course.json")["id"] == manifest["tracks"][0]["legacy_id"] == "tsi-math"
    ids = set()
    count = 0
    for record in manifest["tracks"][1:]:
        path = ROOT / record["content"]
        assert path.is_file(), path
        track = read(record["content"])
        assert track["id"] == record["id"]
        assert track["official_questions"] is False
        assert track["official_score_prediction"] is False
        assert track["reference"].startswith("https://")
        assert track["topics"]
        for topic in track["topics"]:
            assert topic["id"] not in ids
            ids.add(topic["id"])
            assert topic["title"] and topic["description"] and topic["questions"]
            for question in topic["questions"]:
                assert question["id"] not in ids, question["id"]
                ids.add(question["id"])
                assert len(question["prompt"]) >= 20
                assert len(question["options"]) == 4
                assert len(set(question["options"])) == 4
                assert isinstance(question["correct"], int)
                assert 0 <= question["correct"] < 4
                assert len(question["explanation"]) >= 16
                count += 1
    assert count == 20, count
    print(f"PASS: three sample exam tracks, {count} unique questions; legacy TSI unchanged")

if __name__ == "__main__":
    main()
