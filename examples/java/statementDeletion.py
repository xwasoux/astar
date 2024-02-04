import os
import logging
from copy import deepcopy
from astars import AParser, APruner

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
    with open(os.path.join(os.path.dirname(__file__), "input", "java_sample.java")) as f:
        code = f.read()

    java_parser = AParser(lang="java")
    code = java_parser.preprocess(text=code)
    tree = java_parser.parse(text=code)
    logging.info(tree)

    ## Single Node Pruning
    logging.info("<<< Subtree Pruning >>>")
    logging.info(f"Original code: \n{tree.recover()}")
    res = APruner.sequencialSubtreePrune(tree=tree)
    for east in res:
        logging.info(f"\n{east[0].recover()}")
    
    ## Selected Type Pruning
    logging.info("<<< Selected Subtree Pruning >>>")
    logging.info(f"Original code: \n{tree.recover()}")
    selections = ["if_statement", "elif_clause", "else_clause", "for_statement", "while_statement"]
    logging.info(f"Selections of Node Type: {selections}")
    res = APruner.selectedSubtreePrune(tree=tree, selections=selections)
    for east in res:
        logging.info(f"\n{east[0].recover()}")

if __name__ == "__main__":
    main()