from anytree import Walker
from anytree import PreOrderIter, PostOrderIter

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

class ANodeTraverser:
    def __init__(self) -> None:
        pass

    def walk(self, target:str="all") -> list:
        if target=="all":
            pass
        elif target=="subunit":
            pass

    @staticmethod
    def preOrder(root, target:str, reversal:bool=False):
        def __preOrder(node, target:str, reversal:bool=False):
            def __nodeCatchCond(node, target:str):
                if target=="all":
                    result.append(node)
                elif target=="named":
                    if node.is_named:
                        result.append(node)
                elif target=="subunit":
                    if node.type in subUnitName:
                        result.append(node)
                
            if reversal is False:
                for child in node.children:
                    __nodeCatchCond(node=child, target=target)
                    __preOrder(node=child, reversal=reversal)
            elif reversal is True:
                for child in reversed(node.children):
                    __nodeCatchCond(node=child, target=target)
                    __preOrder(node=child, target=target, reversal=reversal)
            
        result = []
        __preOrder(node=root, target=target, reversal=reversal)
        return result
            

    @staticmethod
    def postOrder(root, target:str, reversal:bool=False) -> list:
        def __postOrder(node, target:str, reversal:bool=False) -> None:
            def __nodeCatchCond(node, target:str) -> None:
                nonlocal result
                if target=="all":
                    result.append(node)
                elif target=="named":
                    if node.is_named:
                        result.append(node)
                elif target=="subunit":
                    if node.type in subUnitName:
                        result.append(node)
                return None
                
            nonlocal result
            if reversal is False:
                for child in node.children:
                    __postOrder(node=child, target=target, reversal=reversal)
                __nodeCatchCond(node=node, target=target)
            elif reversal is True:
                for child in reversed(node.children):
                    __postOrder(node=child, target=target, reversal=reversal)
                __nodeCatchCond(node=node, target=target)
            return None
            
        result = []
        __postOrder(root, target, reversal)
        return result