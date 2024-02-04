import os
from astars import AParser

def main():
    with open(os.path.join(os.path.dirname(__file__), "input", "python_sample.py")) as f:
        code = f.read()

    # py_parser = AParser(lang="python")
    ## If you want to build the parser to your local directory, use the following code
    py_parser = AParser(lang="python", build_to=os.path.join(os.path.dirname(__file__)))
    code = py_parser.preprocess(text=code)
    tree = py_parser.parse(text=code)
    print(tree)
    print(tree.originalCode)

    return None


if __name__ == "__main__":
    main()