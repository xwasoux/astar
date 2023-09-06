from anytree import RenderTree

from ..nodes import ANode

class Basetree:
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        self.root = tree
        self.originalCode = code
        self.language = lang

        self.shreddedCode = _splitText(code)

    def __str__(self) -> str:
        return RenderTree(self.root).by_attr("type")

    def textUpdate(self) -> str:
        return 




class AParseTree(Basetree):
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        super().__init__(tree, code, lang)

class AEditedParseTree(Basetree):
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