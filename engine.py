#The main engine for the mini-text-search project. Handles indexing and searching functionality.
from utils import tokenize
import sys
import json
from pathlib import Path

def tokenize_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = tokenize(f.read())
        return content

def analyze_file(file_path, results):
    results["total_files"] += 1
    results["analyzed_files"].append(str(file_path))
    local_result = tokenize_file(file_path)
    for local_word in local_result:
        results["index"].setdefault(local_word, []).append(str(file_path))

def build_index(path):
    general_result = {
        "total_files": 0,
        "analyzed_files": [],
        "index": {}
        }

    p = Path(path)
    if not p.exists():
        print(f"The folder or file '{path}' does not exist.")
        sys.exit(1)
    if p.is_dir():
        for file_path in Path(path).rglob("*.txt"):
            analyze_file(file_path, general_result)

    elif p.is_file() and p.suffix == ".txt":
        analyze_file(p, general_result)
    else:
        print(f"'{path}' is not a valid file or folder.")
        sys.exit(1)
    print(json.dumps(general_result, indent=4))


def search(query):
    print(f"Searching for query: {query}")