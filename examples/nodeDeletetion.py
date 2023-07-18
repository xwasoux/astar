from os import path
import logging
from copy import deepcopy
from astars import AParser, AstAnalyser, AstOperator, ACodeGenerator
from anytree import RenderTree

logging.basicConfig(format='%(asctime)s -\n %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    parser = AParser()
    tree = parser.parse(text=code, lang="python")
    logging.info(RenderTree(tree).by_attr("type"))

    analyser = AstAnalyser(tree=tree)
    subunitNodeList = analyser.subunitNodes()

    operator = AstOperator()
    generator = ACodeGenerator()
    logging.info(generator.generate(root=tree))

    duplicatedTree = deepcopy(tree)

    for subtree in reversed(subunitNodeList):
        editedTree = operator.delete(root=duplicatedTree, target=subtree)
        logging.info(generator.generate(root=editedTree))

if __name__ == "__main__":
    main()
