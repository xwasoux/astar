from ..nodes.node import ANode

allAttr = [
    "child_by_field_id", "child_by_field_name", "child_count", 
    "children", "children_by_field_id", "children_by_field_name", 
    "end_byte", "end_point", "field_name_for_child", 
    "has_changes", "has_error", "id", 
    "is_missing", "is_named", "named_children_count", 
    "named_children", "next_named_sibling", "next_sibling",
    "parent", "prev_named_sibling", "prev_sibling", 
    "sexp", "start_byte", "start_point", 
    "text", "type", "walk"
    ]

tempAttr = [
    "child_by_field_id", "child_by_field_name", 
    "children_by_field_id", "end_byte", "end_point",
    "has_changes", "has_error", "id", 
    "is_missing", "is_named", 
    "sexp", "start_byte", "start_point", 
    "text", "type", "walk"
    ]

def _addNode(source, parent=None):
    sourceAttrs = dir(source)
    filterdAttrs = [attr for attr in sourceAttrs if attr in tempAttr]
    dictAttrs = {attr:getattr(source, attr) for attr in filterdAttrs}
        
    return ANode(name=str(dictAttrs["id"]), parent=parent, dictAttrs=dictAttrs)