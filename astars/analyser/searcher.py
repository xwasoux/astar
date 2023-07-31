from ..nodes import ANode
from anytree import find, find_by_attr, findall, findall_by_attr

class ASearcher:
    
    @staticmethod
    def searchNode(tree:ANode, id:str) -> ANode:
        return find_by_attr(tree, id)
    
    @staticmethod
    def searchAllNode(tree:ANode, id:str) -> ANode:
        return findall_by_attr(tree, id)