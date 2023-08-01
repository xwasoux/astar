from os import path
from astars import AParser, AstAnalyser

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    tree = AParser.parse(text=code, lang="python")
    print(tree)

    return None


if __name__ == "__main__":
    main()