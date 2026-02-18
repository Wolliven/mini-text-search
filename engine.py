#The main engine for the mini-text-search project. Handles indexing and searching functionality.
from utils import tokenize
import sys
import json
from pathlib import Path
import argparse

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
    open("index.json", "w", encoding='utf-8').write(json.dumps(general_result, indent=4))
    print(f"Index built successfully. Total files indexed: {general_result['total_files']}")


def search(query_words, mode="and"):
    try:
        with open("index.json", "r", encoding='utf-8') as f:
            index_data = json.load(f)
    except FileNotFoundError:
        print("Index file not found. Please run 'python index.py <folder_path>' to create the index first.")
        sys.exit(1)

    query_tokens = tokenize(" ".join(query_words))
    matching_files = set()

    print(f"Searching for: {query_tokens} with mode: {mode}")
    if mode == "and":
        matching_files = set(index_data["index"].get(query_tokens[0], []))
        for token in query_tokens[1:]:
            if token in index_data["index"]:
                matching_files.intersection_update(index_data["index"][token])
            else:
                matching_files.clear()
                break
    elif mode == "or":
        for token in query_tokens:
            if token in index_data["index"]:
                matching_files.update(index_data["index"][token])

    if matching_files:
        print("Files matching the query:")
        for file in matching_files:
            print(file)
    else:
        print("No files match the query.")