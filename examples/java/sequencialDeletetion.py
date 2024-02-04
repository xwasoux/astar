import os
import logging
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

    ## Forward Sequencial Pruning
    logging.info("<<< Forward Sequencial Pruning >>>")
    logging.info(f"Original: \n{tree.recover()}")
    res = APruner.sequencialForwardPrune(tree=tree)
    for east in res:
        logging.info(f"\n{east[0].recover()}")

    ## Backward Sequencial Pruning
    logging.info("<<< Backward Sequencial Pruning >>>")
    logging.info(f"Original: \n{tree.recover()}")
    res = APruner.sequencialBackwardPrune(tree=tree)
    for east in res:
        logging.info(f"\n{east[0].recover()}")


if __name__ == "__main__":
    main()