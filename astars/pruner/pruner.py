from copy import deepcopy

from ..nodes import ANode
from ..tree import AParseTree
from ..traverser import ATraverser, AReverseTraverser

class APruner:

    @staticmethod
    def sequencialForwardPrune(tree:AParseTree) -> tuple:
        return _sequencialCodeDlete(tree=tree, reversal=False)

    @staticmethod
    def sequencialBackwardPrune(tree:AParseTree) -> tuple:
        return _sequencialCodeDlete(tree=tree, reversal=True)

    @staticmethod
    def sequencialSubtreePrune(tree:AParseTree) -> tuple:
        return _pointingCodeDelete(tree=tree)
    
    @staticmethod
    def selectedSubtreePrune(tree:AParseTree, selections:list) -> tuple:
        return _pointingCodeDelete(tree=tree, selections=selections)


def _sequencialCodeDlete(tree:AParseTree, reversal:bool) -> tuple:
    duplicatedTree = deepcopy(tree)

    if not reversal:
        traverseRes = ATraverser()
        traverseRes.postorderTraverse(tree=duplicatedTree)
    elif reversal:
        traverseRes = AReverseTraverser()
        traverseRes.postorderTraverse(tree=duplicatedTree)

    allNodetuple = traverseRes.postAllNodes

    res = []
    for targetNode in allNodetuple:
        if not targetNode.is_root:
            editedTree = duplicatedTree.delete(nodeObj=targetNode)
            res.append(deepcopy(editedTree))
    return tuple(res)


def _pointingCodeDelete(tree:AParseTree, selections:tuple=None) -> tuple:

    if selections:
        selectedNodetuple = []
        for ntype in selections:
            selectedNodetuple.extend(tree.searchNodeByType(ntype))
    elif selections == None:
        traverseRes = ATraverser()
        traverseRes.postorderTraverse(tree=tree)
        selectedNodetuple = traverseRes.postAllNodes
    
    res = []
    for node in selectedNodetuple:
        duplicatedTree = deepcopy(tree)

        if not node.is_root:
            editedTree = duplicatedTree.delete(nodeID=node.name)
            res.append(editedTree)

    return tuple(res)
