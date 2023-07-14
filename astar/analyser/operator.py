import anytree
from astar import ANode

class AstOperator:
    def __init__(self) -> None:
        pass

    def insert(self, root:ANode, target:ANode, subtree:ANode) -> ANode:
        subtree.parent = target
        return root

    def delete(self, root:ANode, target:ANode) -> ANode:
        targetParent = target.parent
        target.parent = None
        return root

    def replace(self, root:ANode, target:ANode, subtree:ANode) -> ANode:
        targetParent = target.parent
        target.parent = None
        subtree.parent = targetParent
        return root