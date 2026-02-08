import arkadia.ai as ai
from arkadia.ai.data import SchemaKind
from utils import assert_roundtrip

# ==============================================================================
# 1. SCHEMA DEFINITION META (Types defined in < ... >)
# ==============================================================================

def test_different_type_in_record():
    aid_text = """
    < 
      id: number
    >
    ( ["text"] )
    """

    
    result = ai.data.decode(aid_text)
    node = result.node
    errors = result.errors
    assert len(errors) == 0
    
    # 1. Check Record Meta (Outer)
    assert node.is_record

    excepted = '<id:number>(<[string]> ["text"])'
    assert_roundtrip(node, excepted, True)


def test_simple_types():
    aid_text = '{ a:"a", b:"b", c:"c", d: 3 }'
    excepted = '<a:string,b:string,c:string,d:number>("a","b","c",3)'
    assert_roundtrip(aid_text, excepted, True)   
    

def test_record_named_type_mismatch():
    """
    Tests a scenario where a positional record field has a defined type (e.g., string),
    but the actual value inside is of a different type (e.g., int).

    This ensures that the _record method in Encoder uses _apply_type_tag correctly.

    Schema: <test: string>
    Data: (3)
    Expected Output: (<number> 3)
    """

    # 1. Input in AID format
    aid_text = """
<tests: string>
{
 tests: 3
}
    """

    excepted = '<tests:string>(<number> 3)'
    assert_roundtrip(aid_text, excepted, True)   


def test_record_positional_type_mismatch():
    """
    Tests a scenario where a positional record field has a defined type (e.g., string),
    but the actual value inside is of a different type (e.g., int).

    This ensures that the _record method in Encoder uses _apply_type_tag correctly.

    Schema: <test: string>
    Data: (3)
    Expected Output: (<number> 3)
    """

    # 1. Input in AID format
    aid_text = """
<tests: string>
(3)
    """

    excepted = '<tests:string>(<number> 3)'
    assert_roundtrip(aid_text, excepted, True)   














# # TODO: Change meta how it divide
# # <  / meta list /
# # [  /meta element in list /  @key=4 !required  id: int,
# #    name: string ] >
# #     [
# #       / meta about data /
# #       / meta obabout first object or just type/ !required  @info (1, "Alice")
# #       (2, "Bob")
# #     ]


# # TODO: Chanve meta how it divides
# # <  / meta list /
# # [  /meta element in list /  @key=4 !required  id: int,
# #    name: string ] >
# #     [
# #       / meta about data @size=3 /
# #       / meta obabout first object or just type/ !required  @info  3,
# #       "32",
# #       534
# #     ]


# # TODO: PRIVITIE LISTS SHOULD HAVE COMMA,
# # COMMA IS REQUIRED IN DATA
# #         return self._join(out, "\n") this is wrong in Encoder it should have ","


# def test_meta_schema_field_modifiers():
#     """
#     Tests field modifiers inside a record definition: !required, @key=value.
#     """
#     aid_text = """
#     <
#         !required 
#         @key=101 
#         id: int,

#         @desc="User Name"
#         name: string
#     >
#     ( 1, "Alice" )
#     """
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
#     assert node.is_record # Root is a record because input uses (...)
    
#     # Retrieve field definitions from schema
#     fields = node.schema.fields
    
#     # Field 'id'
#     f_id = next(f for f in fields if f.name == "id")
#     assert f_id.required is True
#     assert getattr(f_id, "meta", {}).get("key") == 101
    
#     # Field 'name'
#     f_name = next(f for f in fields if f.name == "name")
#     # Default is required=False (if !required is missing)
#     assert f_name.required is False 
#     assert getattr(f_name, "meta", {}).get("desc") == "User Name"


# # ==============================================================================
# # 2. DATA BLOCK META (Metadata inside data blocks [ ... ])
# # ==============================================================================

# def test_meta_data_block_list_primitive():
#     """
#     Tests metadata inside a data block for a simple list.
#     Syntax: [ / @size=3 / 1, 2, 3 ]
#     """
#     aid_text = '[ / @size=3 @author="me" / 1, 2, 3 ]'
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
    
#     assert node.is_list
#     # Meta should go to this specific node's schema
#     meta = getattr(node.schema, "meta", {})
#     assert meta.get("size") == 3
#     assert meta.get("author") == "me"
    
#     # Check content
#     assert len(node.elements) == 3
#     assert node.elements[0].value == 1


# def test_meta_data_block_list_of_records():
#     """
#     Tests metadata in a data block that contains a list of records.
#     We have a type definition upfront, but the data block has its own meta (e.g., pagination).
#     """
#     aid_text = """
#     < [ id: int ] >
#     [ 
#       / @page=1 @total=100 /
#       (1), (2)
#     ]
#     """
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
    
#     assert node.is_list
    
#     # Check if "runtime" metadata (page, total) is available
#     meta = getattr(node.schema, "meta", {})
#     assert meta.get("page") == 1
#     assert meta.get("total") == 100
    
#     # Check if the element type is still correct (from definition <...>)
#     assert node.schema.element.kind == SchemaKind.RECORD


# # ==============================================================================
# # 3. NESTED META (Lists within lists)
# # ==============================================================================

# def test_meta_nested_lists():
#     """
#     Tests metadata assignment in nested lists.
#     Structure: [ /@level=0/  [ /@level=1/ 1, 2 ] ]
#     """
#     aid_text = """
#     [ 
#       / @level=0 /
#       [ 
#         / @level=1 / 
#         1, 2 
#       ],
#       [
#         / @level=1 /
#         3, 4
#       ]
#     ]
#     """
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
    
#     # Root Node
#     assert node.is_list
#     assert getattr(node.schema, "meta", {}).get("level") == 0
    
#     # Inner Node 1
#     inner1 = node.elements[0]
#     assert inner1.is_list
#     assert getattr(inner1.schema, "meta", {}).get("level") == 1
    
#     # Inner Node 2
#     inner2 = node.elements[1]
#     assert inner2.is_list
#     assert getattr(inner2.schema, "meta", {}).get("level") == 1


# # ==============================================================================
# # 4. EDGE CASES & OVERRIDES
# # ==============================================================================

# def test_meta_mixed_with_type_override():
#     """
#     Tests a scenario where we have metadata for the list AND a type override for an element.
#     """
#     aid_text = '[ / @info="mixed" / 1, 2, <string> "3" ]'
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
    
#     # List Meta
#     assert getattr(node.schema, "meta", {}).get("info") == "mixed"
    
#     # List Type Inference (Should be Number/Int based on first element '1')
#     assert node.schema.element.type_name in ["number", "int"]
    
#     # Element Override
#     el_last = node.elements[2]
#     assert el_last.schema.type_name == "string"
#     assert el_last.value == "3"


# def test_meta_and_explicit_type_in_data():
#     """
#     Tests a scenario where an explicit type is provided inside the / ... / block.
#     [ / @tag=1 int / 1, 2 ]
#     The parser must understand that 'int' is the list type, and @tag is metadata.
#     """
#     aid_text = '<[string]> / @meta=3 / [ <number> 1, <number> 2 ]'
    
#     node, errors = ai.data.decode(aid_text)
#     assert len(errors) == 0
    
#     assert node.is_list
#     assert node.schema.element.type_name == "int"
#     assert getattr(node.schema, "meta", {}).get("tag") == 1