import json
from typing import Any, Dict, List

def snake_to_camel(snake_case_string):
    components = snake_case_string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def convert_keys_to_camel(dct, reserved_keys=None, reserved_prefixes=None):
    if reserved_keys is None:
        reserved_keys = ["", "discount_ceshi0220"]
    if reserved_prefixes is None:
        reserved_prefixes = []


    if isinstance(dct, dict):
        return {
            convert_key_if_not_reserved(k, reserved_keys, reserved_prefixes): convert_keys_to_camel(v, reserved_keys)
            for k, v in dct.items()
        }
    elif isinstance(dct, list):
        return [convert_keys_to_camel(x, reserved_keys) for x in dct]
    else:
        return dct

def convert_key_if_not_reserved(key, reserved_keys, reserved_prefixes):
    if key in reserved_keys or any(key.startswith(prefix) for prefix in reserved_prefixes):
        return key
    else:
        return snake_to_camel(key)


def is_numeric(val: Any) -> bool:
    return isinstance(val, (int, float))

def compare_json(new_json_str, old_json_str, compare_values=True):
    new_json = json.loads(new_json_str)
    old_json = json.loads(old_json_str)

    converted_old_json = convert_keys_to_camel(old_json)

    def recursive_compare(new_obj, old_obj, path=""):
        if isinstance(new_obj, dict) and isinstance(old_obj, dict):
            new_keys = set(new_obj.keys())
            old_keys = set(old_obj.keys())
            added_keys = new_keys - old_keys
            removed_keys = old_keys - new_keys
            common_keys = new_keys & old_keys

            for key in added_keys:
                print(f"{path}{key}: 新增")
            for key in removed_keys:
                print(f"{path}{key}: 移除")

            for key in common_keys:
                new_val = new_obj[key]
                old_val = old_obj[key]
                next_path = f"{path}{key}."

                if is_numeric(new_val) and is_numeric(old_val):
                    if round(new_val) != round(old_val):
                        print(f"{next_path[:-1]}: 新值 -> {new_val}, 旧值 -> {old_val}")
                else:
                    recursive_compare(new_val, old_val, next_path)

        elif isinstance(new_obj, list) and isinstance(old_obj, list):
            for i, (new_item, old_item) in enumerate(zip_longest(new_obj, old_obj, fillvalue=None)):
                next_path = f"{path}[{i}]"

                if new_item is None or old_item is None or new_item != old_item:
                    if is_numeric(new_item) and is_numeric(old_item):
                        if round(new_item) != round(old_item):
                            print(f"{next_path}: 新值 -> {new_item}, 旧值 -> {old_item}")
                    else:
                        recursive_compare(new_item, old_item, next_path)

    from itertools import zip_longest

    recursive_compare(new_json, converted_old_json)

if __name__ == '__main__':
    # 示例：

    new_json_str = '{"person": {"firstName": "John", "age": 30.0, "children": [{"name": "Child1", "age": 5.5}]}}'
    old_json_str = '{"person": {"first_name": "Jane", "age": 29.999, "children": [{"name": "child1", "age": 5}]}}'

    new_json = json.loads(new_json_str)
    old_json = json.loads(old_json_str)
    converted_old_json = convert_keys_to_camel(old_json)

    print("converted_old_json:", converted_old_json)

    compare_json(new_json_str, old_json_str)