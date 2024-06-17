import unittest
from src.regex_parser import parse_regex

class TestParseRegex(unittest.TestCase):
    def test_single_character(self):
        result = parse_regex("a")
        expected = ['a']
        self.assertEqual(result, expected)

    def test_concatenation(self):
        result = parse_regex("ab")
        expected = [('a', '.', 'b')]
        self.assertEqual(result, expected)

    def test_union(self):
        result = parse_regex("a|b")
        expected = [('a', '|', 'b')]
        self.assertEqual(result, expected)

    def test_closure(self):
        result = parse_regex("a*")
        expected = [('a', '*')]
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        result = parse_regex("a(b|c)*d")
        expected = [('a', '.', ((('b', '|', 'c'), '*'), '.', 'd'))]
        self.assertEqual(result, expected)

    def test_nested_parentheses(self):
        result = parse_regex("(a(b|c))")
        expected = [('a', '.', ('b', '|', 'c'))]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
