import logging
import anytree
from anytree import RenderTree

from ..nodes import ANode
from .traverse import AllNodeTraverser

class AstAnalyser:

    @staticmethod
    def print(tree) -> None:
        _print(tree, "type")
        return None

    @staticmethod
    def printID(tree) -> None:
        _print(tree, "id")
        return None

def _print(tree:ANode, attr:str) -> None:
    logging.basicConfig(format='%(message)s',
                        level=logging.INFO)
    logging.info(RenderTree(tree).by_attr(attr))
    return None
