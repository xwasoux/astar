from ..nodes import ANode

class ACodeGenerator:
    def __init__(self) -> None:
        pass

    def generate(self, root:ANode) -> str:
        codeList = root.textList
        recoveredCode = ""
        recoveredCodeList = []

        for line in codeList:
            for column in line:
                if column != None:
                    recoveredCodeList.append(column)
        recoveredCode = "".join(recoveredCodeList)
        return recoveredCode