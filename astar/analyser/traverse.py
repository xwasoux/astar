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

    def preOrder(self, root, target:str="named"):
        if target=="all":
            return [node for node in PreOrderIter(root)]
        elif target=="named":
            return [node for node in PreOrderIter(root) if node.is_named]
        elif target=="subunit":
            return [node for node in PreOrderIter(root) if node.type in subUnitName]

    def postOrder(self, root, target:str="named"):
        if target=="all":
            return [node for node in PostOrderIter(root)]
        elif target=="named":
            return [node for node in PostOrderIter(root) if node.is_named]
        elif target=="subunit":
            return [node for node in PostOrderIter(root) if node.type in subUnitName]