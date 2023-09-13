from os import path
import logging
from copy import deepcopy
from astars import AParser, APruner

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    tree = AParser.parse(text=code, lang="python")
    logging.info(tree)

    ## Single Node Pruning
    logging.info("<<< Single Node Pruning >>>")
    logging.info(f"Original code: \n{tree.recover()}")
    pointRes = APruner.seqPointingPrune(tree=tree)
    for east in pointRes:
        logging.info(f"\n{east[0].recover()}")

    
    ## Selected Type Pruning
    logging.info("<<< Selected Type Pruning >>>")
    logging.info(f"Original code: \n{tree.recover()}")
    selections = ["if_statement", "elif_clause", "else_clause", 
                "for_statement", "while_statement"]
    logging.info(f"Selections of Node Type: {selections}")
    selectPointRes = APruner.selectedPointingPrune(tree=tree, selections=selections)
    for east in selectPointRes:
        logging.info(f"\n{east[0].recover()}")

if __name__ == "__main__":
    main()
