import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "concept_knowledge.json"

def load_knowledge_base():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def build_topic_lookup():
    data = load_knowledge_base()
    lookup = {}
    for item in data["topics"]:
        lookup[item["topic"]] = item
    return lookup

if __name__ == "__main__":
    kb = load_knowledge_base()
    print(f"Loaded {len(kb['topics'])} concepts from {DATA_FILE}")
