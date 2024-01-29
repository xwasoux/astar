from os import path
from astars import AParser

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    py_parser = AParser(lang="python")
    ## If you want to build the parser to your local directory, use the following code
    # py_parser = AParser(lang="python", build_to=os.path.join(os.path.dirname(__file__)))
    tree = py_parser.parse(text=code)
    print(tree)

    return None


if __name__ == "__main__":
    main()