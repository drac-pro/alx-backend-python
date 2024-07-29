#!/usr/bin/env python3
"""defines a test class to test utils.access_nested_map"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map function from the utils module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map with different parameters"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
