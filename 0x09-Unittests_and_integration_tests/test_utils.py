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
from unittest.mock import Mock, patch
from utils import get_json, access_nested_map, memoize


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
        [{}, ("a",), "a"],
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


class TestGetJson(unittest.TestCase):
    """[TestGetJson class]
    """
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    @patch("utils.get_json")
    def test_get_json(self, test_url: str, test_payload: dict, m: Mock):
        """[summary]

        Args:
            test_url (str): [description]
            test_payload (dict): [description]
            m (Mock): [description]
        """
        m.json.return_value = test_payload
        with patch("requests.get", return_value=m) as p:
            self.assertEqual(get_json(test_url), test_payload)
            p.method.asset_called_once()


class TestMemoize(unittest.TestCase):
    """[TestMMemoize class]
    """
    def test_memoize(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as m:
            m.return_value = 42
            test = TestClass()
            self.assertEqual(test.a_property, m.return_value)
            self.assertEqual(test.a_property, m.return_value)
            m.assert_called_once()
