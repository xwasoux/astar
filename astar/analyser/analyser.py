import anytree
from .traverse import ANodeTraverser

class AstAnalyser:
    def __init__(self, tree) -> None:
        self.tree = tree

    def allNodes(self) -> list:
        visitor = ANodeTraverser()
        return visitor.preOrder(self.tree, target="all")

    def namedNodes(self) -> list:
        visitor = ANodeTraverser()
        return visitor.preOrder(self.tree)

    def subunitNodes(self) -> list:
        visitor = ANodeTraverser()
        return visitor.preOrder(self.tree, target="subunit")
