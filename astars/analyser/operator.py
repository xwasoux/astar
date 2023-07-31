import anytree
from ..nodes import ANode
from .updater import Aupdater


def rootmuch(func):
    def wrapper(*args, **kwargs):
        root = kwargs["root"]
        droot = kwargs["target"].root

        if root == droot:
            return func(*args, **kwargs)
        else:
            raise Exception("Tree objects are not identical! Cheke the arguments.")
    return wrapper


class AstOperator:

    def insert(self, root:ANode, target:ANode, subtree:ANode) -> ANode:
        subtree.parent = target
        return root

    @staticmethod
    @rootmuch
    def delete(root:ANode, target:ANode) -> ANode:
        targetParent = target.parent
        target.parent = None

        updater = Aupdater()
        updater.textDelete(root=root, target=target, parent=targetParent)
        return root

    def replace(self, root:ANode, target:ANode, subtree:ANode) -> ANode:
        targetParent = target.parent
        target.parent = None
        subtree.parent = targetParent
        return root