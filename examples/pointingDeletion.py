from os import path
import logging
from copy import deepcopy
from astars import AParser, AllNodeTraverser, ANamedTraverser, AIDTraverser, AstAnalyser, AstOperator, ACodeGenerator

logging.basicConfig(format='%(asctime)s -\n %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    parser = AParser()
    tree = parser.parse(text=code, lang="python")
    AstAnalyser.print(tree)

    logging.info(ACodeGenerator.generate(root=tree))

    pointRes = AstAnalyser.pointingCodeDelete(tree)
    for east in pointRes:
        AstAnalyser.print(east)


if __name__ == "__main__":
    main()
