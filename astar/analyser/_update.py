from ..nodes import ANode

def _textDeleteOneLine(codeList:list, lineNum:int, columnStart:int, columnEnd:int) -> None:
    targetLine = codeList[lineNum]

    deleteStrSize = columnEnd - columnStart
    targetLine[columnStart:columnEnd] = [None for _ in range(deleteStrSize)]
    return None

def _textDeleteMultiLine(codeList:list, posStart:tuple, posEnd:tuple) -> None:
    lineStart, columnStart = posStart
    lineEnd, columnEnd = posEnd
    
    mode = "pass"
    for lNum, line in enumerate(codeList):
        for cNum, _ in enumerate(line):
            if (lNum == lineStart) and (cNum == columnStart):
                mode = "None"
            elif (lNum == lineEnd) and (cNum == columnEnd):
                mode = "pass"

            if mode == "pass":
                pass
            elif mode == "None":
                line[cNum] = None
    return None

def _textDelete(root, posStart:tuple, posEnd:tuple) -> None:
    codeList = root.textList

    if posStart[0] == posEnd[0]:
        _textDeleteOneLine(codeList, posStart[0], posStart[1], posEnd[1])
    else:
        _textDeleteMultiLine(codeList, posStart, posEnd)
    
    return None

def _textDeletePropergation(root, parent:ANode, posStart:tuple, posEnd:tuple) -> None:
    codeList = str(root.textList)
    pass