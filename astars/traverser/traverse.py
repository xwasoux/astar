from ..nodes import ANode
from ..tree import AParseTree

class ATraverser:

    def __init__(self) -> None:
        pass
    
    def preorderTraverse(self, tree:AParseTree) -> "ATraverser":
        def __preOrder(node:ANode) -> None:
            for child in node.children:
                self.preAllNodes.append(child)
                self.preNodeTypes.append(child.type)
                self.preNodeNames.append(child.name)
                self.preNodeIds.append(child.id)
                __preOrder(node=child)
            return None
            
        self.preAllNodes = [tree.root]
        self.preNodeTypes = [tree.root.type]
        self.preNodeNames = [tree.root.name]
        self.preNodeIds = [tree.root.id]

        __preOrder(node=tree.root)
        return self
            
    def postorderTraverse(self, tree:AParseTree) -> "ATraverser":
        def __postOrder(node:ANode) -> None:
            for child in node.children:
                __postOrder(node=child)
            self.postAllNodes.append(node)
            self.postNodeTypes.append(node.type)
            self.postNodeNames.append(node.name)
            self.postNodeIds.append(node.id)
            return None
            
        self.postAllNodes = []
        self.postNodeTypes = []
        self.postNodeNames = []
        self.postNodeIds = []

        __postOrder(tree.root)
        return self

class AReverseTraverser:

    def __init__(self) -> None:
        pass
    
    def preorderTraverse(self, tree:AParseTree) -> "AReverseTraverser":
        def __preOrder(node:ANode) -> None:
            for child in reversed(node.children):
                self.preAllNodes.append(child)
                self.preNodeTypes.append(child.type)
                self.preNodeNames.append(child.name)
                self.preNodeIds.append(child.id)
                __preOrder(node=child)
            return None
            
        self.preAllNodes = [tree.root]
        self.preNodeTypes = [tree.root.type]
        self.preNodeNames = [tree.root.name]
        self.preNodeIds = [tree.root.id]

        __preOrder(node=tree.root)
        return self
            
    def postorderTraverse(self, tree:AParseTree) -> "AReverseTraverser":
        def __postOrder(node:ANode) -> None:
            for child in reversed(node.children):
                __postOrder(node=child)
            self.postAllNodes.append(node)
            self.postNodeTypes.append(node.type)
            self.postNodeNames.append(node.name)
            self.postNodeIds.append(node.id)
            return None
            
        self.postAllNodes = []
        self.postNodeTypes = []
        self.postNodeNames = []
        self.postNodeIds = []

        __postOrder(tree.root)
        return self
