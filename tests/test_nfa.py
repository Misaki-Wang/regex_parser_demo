import unittest
from src.nfa import regex_to_nfa

class TestNFA(unittest.TestCase):
    def test_single_character(self):
        nfa = regex_to_nfa("a")
        self.assertEqual(len(nfa.states), 2)
        self.assertIn('a', nfa.transitions[nfa.start_state])
        self.assertEqual(nfa.transitions[nfa.start_state]['a'][0], nfa.accept_state)

    def test_empty_string(self):
        nfa = regex_to_nfa("")
        self.assertEqual(len(nfa.states), 2)
        self.assertIn('', nfa.transitions[nfa.start_state])
        self.assertEqual(nfa.transitions[nfa.start_state][''][0], nfa.accept_state)

    def test_closure(self):
        nfa = regex_to_nfa("a*")
        self.assertEqual(len(nfa.states), 4)
        self.assertIn('', nfa.transitions[nfa.start_state])
        self.assertIn(nfa.accept_state, nfa.transitions[nfa.start_state][''])

    def test_concatenation(self):
        nfa = regex_to_nfa("ab")
        self.assertEqual(len(nfa.states), 4)
        self.assertIn('a', nfa.transitions[nfa.start_state])
        self.assertIn('b', nfa.transitions[nfa.transitions[nfa.start_state]['a'][0]])

    def test_union(self):
        nfa = regex_to_nfa("a|b")
        self.assertEqual(len(nfa.states), 6)
        self.assertIn('', nfa.transitions[nfa.start_state])
        self.assertIn('a', nfa.transitions[nfa.transitions[nfa.start_state][''][0]])
        self.assertIn('b', nfa.transitions[nfa.transitions[nfa.start_state][''][1]])

    def test_complex_expression(self):
        nfa = regex_to_nfa("a(b|c)*d")
        self.assertTrue(nfa.start_state in nfa.transitions)
        self.assertTrue(nfa.accept_state in nfa.states)
        self.assertTrue(any(nfa.accept_state in targets for targets in nfa.transitions.values()))

if __name__ == "__main__":
    unittest.main()
