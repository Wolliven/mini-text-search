"""
The main engine for the mini-text-search project. Handles indexing and searching functionality.
"""
from utils import tokenize
import json
from pathlib import Path

def tokenize_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return tokenize(f.read())

def analyze_file(file_path, results):
    results["total_files"] += 1
    results["analyzed_files"].append(str(file_path))
    local_result = tokenize_file(file_path)
    for local_word in local_result:
        results["index"].setdefault(local_word, []).append(str(file_path))

def build_index(path, index_path="index.json"):
    general_result = {
        "total_files": 0,
        "analyzed_files": [],
        "index": {}
        }

    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"The folder or file '{path}' does not exist.")
    if p.is_dir():
        for file_path in Path(path).rglob("*.txt"):
            analyze_file(file_path, general_result)

    elif p.is_file() and p.suffix == ".txt":
        analyze_file(p, general_result)
    else:
        raise ValueError(f"'{path}' is not a valid file or folder. Please provide a path to a folder containing text files or a single text file.")
    with open(index_path, "w", encoding='utf-8') as f:
        json.dump(general_result, f, indent=4, ensure_ascii=False)
    return general_result["total_files"]


def search(query_words, mode="and", index_path="index.json"):
    if not Path(index_path).exists():
        raise FileNotFoundError(f"Index file '{index_path}' not found. Please run 'python index.py <folder_path>' to create the index first.")
    if mode not in ["and", "or"]:
        raise ValueError(f"Invalid search mode '{mode}'. Valid modes are 'and' and 'or'.")
    with open(index_path, "r", encoding='utf-8') as f:
        index_data = json.load(f)

    query_tokens = tokenize(" ".join(query_words))
    if not query_tokens:
        raise ValueError("No valid query words provided after tokenization. Please provide one or more valid query words.")
    matching_files = set()
    if mode == "and":
        matching_files = set(index_data["index"].get(query_tokens[0], []))
        for token in query_tokens[1:]:
            matching_files.intersection_update(index_data["index"].get(token, []))
    elif mode == "or":
        for token in query_tokens:
            if token in index_data["index"]:
                matching_files.update(index_data["index"][token])

    return matching_files