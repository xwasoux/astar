import anytree
from .traverse import ANodeTraverser

class AstAnalyser:

    @staticmethod
    def allNodes(root, traversal:str="pre", reverse:bool=False) -> list:
        if traversal == "pre":
            return ANodeTraverser.preOrder(root=root, target="all", reversal=reverse)
        elif traversal == "post":
            return ANodeTraverser.postOrder(root=root, target="all", reversal=reverse)

    @staticmethod
    def namedNodes(root, traversal:str="pre", reverse:bool=False) -> list:
        if traversal == "pre":
            return ANodeTraverser.preOrder(root=root, target="named", reversal=reverse)
        elif traversal == "post":
            return ANodeTraverser.postOrder(root=root, target="named", reversal=reverse)

    @staticmethod
    def subunitNodes(root, traversal:str="pre", reverse:bool=False) -> list:
        if traversal == "pre":
            return ANodeTraverser.preOrder(root=root, target="subunit", reversal=reverse)
        elif traversal == "post":
            return ANodeTraverser.postOrder(root=root, target="subunit", reversal=reverse)
