#Takes the path to a folder containing text files and creates an index.json file
import sys
from engine import build_index

def main(folder_path):
    build_index(folder_path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        query = sys.argv[1]
        main(query)
    else:
        print("Program usage: python index.py <word1> <word2> ...")
        sys.exit(1)