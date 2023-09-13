from anytree import RenderTree
from anytree import find, find_by_attr, findall, findall_by_attr

from ..nodes import ANode
from ._updater import _textDelete, _generate

class AParseTree:
    def __init__(self, tree:ANode, code:str, lang:str) -> None:
        self.root = tree
        self.originalCode = code
        self.language = lang
        self.is_edited = False

        self.shreddedCode = _splitText(code)

    def __str__(self) -> str:
        return RenderTree(self.root).by_attr("type")

    def recover(self) -> str:
        return _generate(self.shreddedCode)

    def delete(self, nodeObj:ANode=None, nodeID:str=None) -> ANode:

        if nodeObj:
            if self.root != nodeObj.root:
                raise Exception("Tree objects are not identical! Check the arguments.")
        elif nodeID:
            nodeObj = self.searchNodeByID(id=nodeID)

        nodeObj.parent = None

        targetPosStart = nodeObj.start_point
        targetPosEnd = nodeObj.end_point

        self.shreddedCode = _textDelete(splittedStrings=self.shreddedCode, 
                                        posStart=targetPosStart, 
                                        posEnd=targetPosEnd)

        self.editedCode = _generate(self.shreddedCode)
        self.is_edited = True

        return (self, nodeObj)

    def searchNodeByID(self, id:str) -> tuple:
        return find_by_attr(node=self.root, value=id)

    def searchNodeByType(self, type:str) -> tuple:
        return findall_by_attr(node=self.root, value=type, name="type")


def _splitText(text:str) -> list:
    lineText = text.splitlines()

    textList = []
    for splitLine in lineText:
        if splitLine == lineText[-1]:
            textList.append(list(splitLine))
        else:
            textList.append(list(splitLine)+["\n"])
        
    return textList