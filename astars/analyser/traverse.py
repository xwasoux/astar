from anytree import Walker
from anytree import PreOrderIter, PostOrderIter

from ..nodes import ANode

subUnitName = [
    "function_definition", 
    "class_definition", 

    "call", 
    "list", 

    "parameters", 
    "default_parameter", 
    "argument_list", 
    "keyword_argument", 
    "assignment", 
    "attribute", 

    "expression_statement",
    "if_statement", 
    "else_clause", 
    "return_statement", 
    
    "binary_operator", 
    "comparison_operator", 
    ]

class AllNodeTraverser:
    ## Pre-Order Traversal
    @staticmethod
    def leftPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                result.append(child)
                __preOrder(node=child)
            return None
            
        result = [root]
        __preOrder(node=root)
        return result
            
    @staticmethod
    def rightPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                result.append(child)
                __preOrder(node=child)
            return None
            
        result = [root]
        __preOrder(node=root)
        return result
            
    
    ## Post-Order Traversal
    @staticmethod
    def leftPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                __postOrder(node=child)
            result.append(node)
            return None
            
        result = []
        __postOrder(root)
        return result

    @staticmethod
    def rightPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                __postOrder(node=child)
            result.append(node)
            return None
            
        result = []
        __postOrder(root)
        return result



class ATypeTraverser:
    ## Pre-Order Traversal
    @staticmethod
    def leftPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                result.append(child.type)
                __preOrder(node=child)
            return None
            
        result = [root.type]
        __preOrder(node=root)
        return result
            
    @staticmethod
    def rightPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                result.append(child.type)
                __preOrder(node=child)
            return None
            
        result = [root.type]
        __preOrder(node=root)
        return result
            
    
    ## Post-Order Traversal
    @staticmethod
    def leftPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                __postOrder(node=child)
            result.append(node.type)
            return None
            
        result = []
        __postOrder(root)
        return result

    @staticmethod
    def rightPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                __postOrder(node=child)
            result.append(node.type)
            return None
            
        result = []
        __postOrder(root)
        return result



class AIDTraverser:
    ## Pre-Order Traversal
    @staticmethod
    def leftPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                result.append(child.id)
                __preOrder(node=child)
            return None
            
        result = [root.id]
        __preOrder(node=root)
        return result
            
    @staticmethod
    def rightPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                result.append(child.id)
                __preOrder(node=child)
            return None
            
        result = [root.id]
        __preOrder(node=root)
        return result
            
    
    ## Post-Order Traversal
    @staticmethod
    def leftPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                __postOrder(node=child)
            result.append(node.id)
            return None
            
        result = []
        __postOrder(root)
        return result

    @staticmethod
    def rightPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                __postOrder(node=child)
            result.append(node.id)
            return None
            
        result = []
        __postOrder(root)
        return result



class ANamedTraverser:
    ## Pre-Order Traversal
    @staticmethod
    def leftPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                if child.is_named:
                    result.append(child)
                __preOrder(node=child)
            return None
            
        result = [root]
        __preOrder(node=root)
        return result
            
    @staticmethod
    def rightPreOrder(root:ANode) -> list:
        def __preOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                if child.is_named:
                    result.append(child)
                __preOrder(node=child)
            return None
            
        result = [root]
        __preOrder(node=root)
        return result
            
    
    ## Post-Order Traversal
    @staticmethod
    def leftPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in node.children:
                __postOrder(node=child)
            if child.is_named:
                result.append(node)
            return None
            
        result = []
        __postOrder(root)
        return result

    @staticmethod
    def rightPostOrder(root:ANode) -> list:
        def __postOrder(node:ANode) -> None:
            nonlocal result
            for child in reversed(node.children):
                __postOrder(node=child)
            if child.is_named:
                result.append(node)
            return None
            
        result = []
        __postOrder(root)
        return result