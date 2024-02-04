import os
import shutil
from typing import Any, Dict, List, Optional, Tuple, Union
from git import Repo
from tree_sitter import Language, Parser, Node

from ..nodes.node import ANode
from ._nodeAdd import _addNode
from ..tree import AParseTree
from ._utils import remove_comments_and_docstrings

class AParser:

    def __init__(self, lang: str, build_to: str = None, force_clone: bool = False) -> None:
        self.lang = lang
        if build_to == None:
            self.parser_dir = os.path.join(os.path.dirname(__file__), "parsers")
        else:
            self.parser_dir = os.path.join(build_to, "parsers")

        if not os.path.exists(self.parser_dir):
            os.makedirs(self.parser_dir)

        self.url = "https://github.com/tree-sitter/tree-sitter-{}.git".format(lang)
        self.clone_dir = os.path.join(self.parser_dir, "tree-sitter-{}".format(self.lang))
        try:
            self.repo = Repo.clone_from(url=self.url, to_path=self.clone_dir)
        except:
            if force_clone:
                if os.path.exists(self.clone_dir):
                    shutil.rmtree(self.clone_dir)
                self.repo = Repo.clone_from(url=self.url, to_path=self.clone_dir)
            print("Repository already exists. If you want to force clone, please set force_clone=True")

        self.LIB_PATH = os.path.join(self.parser_dir, "parser-{}.so".format(self.lang))
        Language.build_library(
            self.LIB_PATH,
            [
                self.clone_dir
            ]
        )

    def preprocess(self, text: str) -> str:
        return remove_comments_and_docstrings(text, self.lang)

    def parse(self, text: str) -> None:
        self.ANY_LANGUAGE = Language(self.LIB_PATH, self.lang)
        parser = Parser()
        parser.set_language(self.ANY_LANGUAGE)

        tree = parser.parse(bytes(text, "utf8"))
        cst = _ts2Anytree(source=tree.root_node, parent=None)

        parsetree = AParseTree(tree=cst, code=text, lang=self.lang)

        return parsetree

def _ts2Anytree(source, parent:ANode=None) -> None:
    if parent == None:
        target = _addNode(source=source)
    else:
        target = _addNode(source=source, parent=parent)

    for child in source.children:
        _ts2Anytree(child, target)

    return target
