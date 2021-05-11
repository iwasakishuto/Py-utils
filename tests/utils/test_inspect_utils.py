# coding: utf-8
def test_get_defined_members():
    from pycharmers.utils import inspect_utils, get_defined_members
    get_defined_members(inspect_utils)
    # {
    #     'get_defined_members': <function pycharmers.utils.inspect_utils.get_defined_members(obj, predicate=<function <lambda> at 0x14227fca0>)>,
    #     'get_import_members': <function pycharmers.utils.inspect_utils.get_import_members(obj)>
    # }

def test_get_import_members():
    from pycharmers.utils import inspect_utils, get_import_members, dumps_json
    print(dumps_json(obj=get_import_members(inspect_utils)))
    # {
    #     "": [
    #         "re",
    #         "inspect"
    #     ],
    #     "collections": [
    #         "defaultdict"
    #     ],
    #     ".generic_utils": [
    #         "str_strip",
    #         "flatten_dual"
    #     ]
    # }

