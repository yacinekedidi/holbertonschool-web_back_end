#!/usr/bin/env python3
"""[test utils module]"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """[class]
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """[summary]

        Args:
            nested_map ([type]): [description]
            path ([type]): [description]
            expected ([type]): [description]
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        [{}, ("a",)], "a",
        [{"a": 1}, ("a", "b"), "b"]
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, inexistant_key: Any):
        """[summary]

        Args:
            nested_map (Mapping): [description]
            path (Sequence): [description]
            inexistant_key (Any): [description]
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
            self.assertEqual(cm.exception, inexistant_key)
