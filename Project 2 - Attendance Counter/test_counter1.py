import unittest
from unittest.mock import patch
from io import StringIO
from counter.counter1 import counter

class TestCounter1(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', 'y', 'n', 'y'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_counter_valid_inputs(self, mock_stdout, mock_input):
        counter()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Students present:  2', output)
        self.assertIn('Students absent:  1', output)

    @patch('builtins.input', side_effect=['3', 'y', 'n', 'maybe'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_counter_invalid_input(self, mock_stdout, mock_input):
        counter()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Invalid input', output)

if __name__ == '__main__':
    unittest.main()