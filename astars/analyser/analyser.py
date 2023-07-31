import logging
from copy import deepcopy
from anytree import RenderTree

from ..nodes import ANode
from .traverse import AllNodeTraverser
from .operator import AstOperator
from .traverse import ATypeTraverser
from .traverse import AIDTraverser
from .searcher import ASearcher

class AstAnalyser:

    @staticmethod
    def print(tree:ANode) -> None:
        _print(tree, "type")
        return None

    @staticmethod
    def printID(tree:ANode) -> None:
        _print(tree, "id")
        return None
    
    @staticmethod
    def printAny(tree:ANode, attr:str) -> None:
        _print(tree, attr)
        return None
    
    @staticmethod
    def forwardSequencialCodeDelete(tree:ANode) -> list:
        return _sequencialCodeDlete(tree, False)

    @staticmethod
    def backwardSequencialCodeDelete(tree:ANode) -> list:
        return _sequencialCodeDlete(tree, True)

    @staticmethod
    def pointingCodeDelete(tree:ANode) -> list:
        return _pointingCodeDelete(tree)

    @staticmethod
    def selectedPointingCodeDelete(tree:ANode, types:list) -> list:
        ids = [node.id for node in ATypeTraverser.leftPostOrder(tree) if node.type in types]
        return _pointingCodeDelete(tree, ids)

    
    
def _sequencialCodeDlete(tree:ANode, reversal:bool) -> list:
    res = []
    dupTree = deepcopy(tree)

    if not reversal:
        allNodeList = AllNodeTraverser.leftPostOrder(dupTree)
    elif reversal:
        allNodeList = AllNodeTraverser.rightPostOrder(dupTree)
    
    for subtree in allNodeList:
        editedTree = AstOperator.delete(root=dupTree, target=subtree)
        res.append(deepcopy(editedTree))
    return res

def _pointingCodeDelete(tree:ANode, selections:list=None) -> list:
    res = []

    if selections == None:
        selections = AIDTraverser.leftPostOrder(tree)
    
    for nodeId in selections:
        dupTree = deepcopy(tree)
        targetNode = ASearcher.searchNode(dupTree, str(nodeId))

        editedTree = AstOperator.delete(root=dupTree, target=targetNode)
        res.append(editedTree)

    return res

def _print(tree:ANode, attr:str) -> None:
    logging.basicConfig(format='%(message)s',
                        level=logging.INFO)
    logging.info(RenderTree(tree).by_attr(attr))
    return None
