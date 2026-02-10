# Mini Text Search Engine

This project is a simple command-line tool that indexes text documents
and allows searching for words across a folder of `.txt` files.

The goal of this project is to learn the fundamentals behind document
indexing and search systems.

---

## Features

- Recursively scans a folder for `.txt` files
- Builds an inverted index mapping words to documents
- Stores the index on disk for reuse
- Allows searching for documents containing given words

---

## Usage

### Index documents

```python index.py <folder_path>```

This command scans the folder and generates an index.json file.

### Search documents

```python search.py <word1> <word2> ...```

This command loads the index and prints the documents that match the given search terms.

---

## Requirements

- Python 3.9 or higher
- No external dependencies

---

## Project scope

This project focuses on:

- basic text normalization
- document indexing
- simple search logic
- persistence using JSON files

Advanced features such as ranking algorithms, NLP techniques, or embeddings are intentionally out of scope.