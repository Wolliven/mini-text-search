#The main engine for the mini-text-search project. Handles indexing and searching functionality.
from utils import normalize
import sys
import json
from pathlib import Path

def build_index(path):
        index = {}
        word_frequency = {}

        p = Path(path)
        if not p.exists():
            print(f"The folder '{path}' does not exist.")
            sys.exit(1)
        if not p.is_dir():
            print(f"'{path}' is not a folder.")
            sys.exit(1)

def search(query):
    print(f"Searching for query: {query}")

