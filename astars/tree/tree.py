from anytree import RenderTree

from ..nodes import ANode

class AParseTree:
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        self.root = tree
        self.originalCode = code
        self.language = lang
        self.is_edited = False

        self.shreddedCode = _splitText(code)

    def __str__(self) -> str:
        return RenderTree(self.root).by_attr("type")

    def textUpdate(self) -> str:
        return 




def _splitText(text:str) -> list:
    lineText = text.splitlines()

    textList = []
    for splitLine in lineText:
        if splitLine == lineText[-1]:
            textList.append(list(splitLine))
        else:
            textList.append(list(splitLine)+["\n"])
        
    return textList