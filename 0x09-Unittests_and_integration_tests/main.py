#!/usr/bin/env python3

access_nested_map = __import__("utils").access_nested_map


print(access_nested_map({"a": {"b": 2}}, path=("a", "b")))
