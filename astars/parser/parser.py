from os import path
from tree_sitter import Language, Parser, Node

from ..nodes.node import ANode
from ._nodeAdd import _addNode
from ..tree import Parsetree

class AParser:

    LIB_PATH = path.join(path.dirname(__file__), "grammar", "tree-sitter", "languages.so")
    Language.build_library(
        LIB_PATH,
        [
            path.join(path.dirname(__file__), "grammar", "tree-sitter", "tree-sitter-python"),
            path.join(path.dirname(__file__), "grammar", "tree-sitter", "tree-sitter-c"),
            path.join(path.dirname(__file__), "grammar", "tree-sitter", "tree-sitter-cpp"),
        ]
    )

    def __init__(self) -> None:
        pass

    @classmethod
    def parse(cls, text:str, lang:str) -> None:
        cls.ANY_LANGUAGE = Language(cls.LIB_PATH, lang)
        parser = Parser()
        parser.set_language(cls.ANY_LANGUAGE)

        tree = parser.parse(bytes(text, "utf8"))
        cst = _ts2Anytree(source=tree.root_node, parent=None)

        parsetree = Parsetree(tree=cst, code=text, lang=lang)

        return parsetree

def _ts2Anytree(source, parent:ANode=None) -> None:
    if parent == None:
        target = _addNode(source=source)
    else:
        target = _addNode(source=source, parent=parent)

    for child in source.children:
        _ts2Anytree(child, target)

    return target
