from ..nodes import ANode
from ._update import _textDelete, _textDeletePropergation

class Aupdater:
    def __init__(self) -> None:
        pass

    def textDelete(self, root:ANode, target:ANode, parent:ANode) -> None:
        targetPosStart = target.start_point
        targetPosEnd = target.end_point

        _textDelete(root=root, 
                    posStart=targetPosStart, 
                    posEnd=targetPosEnd)
        _textDeletePropergation(root=root, 
                                parent=parent, 
                                posStart=targetPosStart, 
                                posEnd=targetPosEnd)
        return None
        