"""
Takes the path to a folder containing text files and creates an index.json file
"""
import sys
from engine import build_index

def main() -> None:
    if len(sys.argv) != 2:
        print("Program usage: python index.py <folder_path or file_path>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        total_files = build_index(path)
        print(f"Index built successfully. Total files indexed: {total_files}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)    

if __name__ == "__main__":
    main()