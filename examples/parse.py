from os import path
from astars import AParser
from anytree import RenderTree

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    parser = AParser()
    tree = parser.parse(text=code, lang="python")
    print(RenderTree(tree).by_attr("type"))

if __name__ == "__main__":
    main()