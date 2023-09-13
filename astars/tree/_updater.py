from ..nodes import ANode


def _textDeleteOneLine(splittedStrings:list, lineNum:int, columnStart:int, columnEnd:int) -> list:
    targetLine = splittedStrings[lineNum]

    deleteStrSize = columnEnd - columnStart
    targetLine[columnStart:columnEnd] = [None for _ in range(deleteStrSize)]
    return splittedStrings

def _textDeleteMultiLine(splittedStrings:list, posStart:tuple, posEnd:tuple) -> list:
    lineStart, columnStart = posStart
    lineEnd, columnEnd = posEnd
    
    mode = "pass"
    for lNum, line in enumerate(splittedStrings):
        for cNum, _ in enumerate(line):
            if (lNum == lineStart) and (cNum == columnStart):
                mode = "None"
            elif (lNum == lineEnd) and (cNum == columnEnd):
                mode = "pass"

            if mode == "pass":
                pass
            elif mode == "None":
                line[cNum] = None
    return splittedStrings

def _textDelete(splittedStrings:list, posStart:tuple, posEnd:tuple) -> list:

    if posStart[0] == posEnd[0]:
        return _textDeleteOneLine(splittedStrings, posStart[0], posStart[1], posEnd[1])
    else:
        return _textDeleteMultiLine(splittedStrings, posStart, posEnd)
    

def _textDeletePropergation(root, parent:ANode, posStart:tuple, posEnd:tuple) -> None:
    splittedStrings = str(root.textList)
    pass
    
def _generate(splittedStrings:list) -> str:
    recoveredCode = ""
    recoveredCodeList = []

    for line in splittedStrings:
        for column in line:
            if column != None:
                recoveredCodeList.append(column)
    recoveredCode = "".join(recoveredCodeList)
    return recoveredCode