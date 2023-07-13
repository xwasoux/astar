from os import path
from tree_sitter import Language, Parser, Node

LIB_PATH = path.join("..", "astar", "parser", "grammar", "tree-sitter", "languages.so")
Language.build_library(
    LIB_PATH,
    [
        path.join("..", "astar", "parser", "grammar", "tree-sitter", "tree-sitter-python"),
        path.join("..", "astar", "parser", "grammar", "tree-sitter", "tree-sitter-c"),
        path.join("..", "astar", "parser", "grammar", "tree-sitter", "tree-sitter-cpp"),
    ]
)

lang = "python"
code = '''
    def max(a, b):
        if a > b:
            return a
        else:
            return b
    '''

ANY_LANGUAGE = Language(LIB_PATH, lang)
parser = Parser()
parser.set_language(ANY_LANGUAGE)

tree = parser.parse(bytes(code, "utf8"))
print(tree)