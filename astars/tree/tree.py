from anytree import RenderTree

from ..nodes import ANode

class Basetree:
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        self.root = tree
        self.code = code
        self.language = lang

        self.codeShredded = _splitText(code)

    def __str__(self) -> str:
        return RenderTree(self.root).by_attr("type")

class Parsetree(Basetree):
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        super().__init__(tree, code, lang)

class EditedParsetree(Basetree):
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        super().__init__(tree, code, lang)


def _splitText(text:str) -> list:
    lineText = text.splitlines()

    textList = []
    for splitLine in lineText:
        if splitLine == lineText[-1]:
            textList.append(list(splitLine))
        else:
            textList.append(list(splitLine)+["\n"])
        
    return textList