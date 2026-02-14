#The main engine for the mini-text-search project. Handles indexing and searching functionality.
from utils import normalize, tokenize
import sys
import json
from pathlib import Path

def analyze_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = tokenize(f.read())
            return content
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while processing the file '{path}': {e}")
        return None

def build_index(path):
    general_result = {
        "total_files": 0,
        "analyzed_files": [],
        "index": {}
        }
    temp_index = {}

    p = Path(path)
    if not p.exists():
        print(f"The folder '{path}' does not exist.")
        sys.exit(1)
    if not p.is_dir():
        print(f"'{path}' is not a folder.")
        sys.exit(1)

    for file_path in Path(path).rglob("*.txt"):
        general_result["total_files"] += 1
        general_result["analyzed_files"].append(str(file_path))
        local_result = analyze_file(file_path)
        for local_word in local_result:
            general_result["index"][local_word] = general_result["index"].get(local_word, []) + [str(file_path)]

    print(json.dumps(general_result, indent=4))

def search(query):
    print(f"Searching for query: {query}")

