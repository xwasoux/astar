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

    selectPointRes = AstAnalyser.selectedPointingCodeDelete(tree, ["if_statement", "elif_clause", "else_clause", 
                                                                   "for_statement", 
                                                                   "while_statement"])
    for east in selectPointRes:
        AstAnalyser.print(east)


if __name__ == "__main__":
    main()