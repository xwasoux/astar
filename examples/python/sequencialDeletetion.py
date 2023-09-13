from os import path
import logging
from astars import AParser, APruner

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
    with open(path.join(path.dirname(__file__), "input", "py_lang.py")) as f:
        code = f.read()

    tree = AParser.parse(text=code, lang="python")

    logging.info(tree)

    ## Forward Sequencial Pruning
    logging.info("<<< Forward Sequencial Pruning >>>")
    logging.info(f"Original: \n{tree.recover()}")
    seqFrontRes = APruner.seqForwardPrune(tree=tree)
    for east in seqFrontRes:
        logging.info(f"\n{east[0].recover()}")

    ## Backward Sequencial Pruning
    logging.info("<<< Backward Sequencial Pruning >>>")
    logging.info(f"Original: \n{tree.recover()}")
    seqBackRes = APruner.seqBackwardPrune(tree=tree)
    for east in seqBackRes:
        logging.info(f"\n{east[0].recover()}")


if __name__ == "__main__":
    main()
