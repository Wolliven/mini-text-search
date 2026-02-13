#Takes the path to a folder containing text files and creates an index.json file
import sys
from engine import build_index

def main(path):
    build_index(path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        main(path)
    else:
        print("Program usage: python index.py <folder_path or file_path>")
        sys.exit(1)