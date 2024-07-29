#!/usr/bin/env python3
"""defines a test class to test utils.access_nested_map"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """tests access_nested_map exceptions"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests get_json function from the utils module"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test get_json with a mock request.get method
        and different parameters
        """
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
