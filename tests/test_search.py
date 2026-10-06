"""Small graph checks, isolated from the desktop-only config module."""
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('search_under_test', Path(__file__).parents[1] / 'algorithms.py')
algorithms = importlib.util.module_from_spec(spec)
with patch.dict(sys.modules, {'config': types.SimpleNamespace(M=1, N=4)}):
    spec.loader.exec_module(algorithms)

class State:
    edges = {'start': [('goal', 10), ('via', 1)], 'via': [('start', 1), ('goal', 1)], 'goal': [], 'dead': []}
    def __init__(self, node='start'):
        self.node = node
    def get_state(self, kind):
        return self.node
    def is_goal_state(self):
        return self.node == 'goal'
    def get_legal_actions(self):
        return self.edges[self.node]
    def generate_successor_state(self, action):
        return State(action[0])
    def get_action_cost(self, action):
        return action[1]

class SearchTests(unittest.TestCase):
    def test_breadth_first_uses_fewest_edges(self):
        self.assertEqual(algorithms.Red().get_path(State()), [('goal', 10)])
    def test_uniform_cost_uses_cheaper_route(self):
        self.assertEqual(algorithms.Black().get_path(State()), [('via', 1), ('goal', 1)])
    def test_goal_and_unreachable(self):
        for cls in (algorithms.Blue, algorithms.Red, algorithms.Black):
            self.assertEqual(cls().get_path(State('goal')), [])
            self.assertIsNone(cls().get_path(State('dead')))

if __name__ == '__main__':
    unittest.main()
