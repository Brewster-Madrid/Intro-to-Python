import unittest
from unittest.mock import patch
from io import StringIO

from counter.counter2 import counter  # Replace 'your_script' with the actual filename

class TestCounter(unittest.TestCase):
    @patch('builtins.input', side_effect=['3', 'Alice', 'Bob', 'Charlie', 'y', 'y', 'n', 'y'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_counter(self, mock_stdout, mock_input):
        counter()
        output = mock_stdout.getvalue()
        
        self.assertIn('Students present:  2', output)
        self.assertIn('Students absent:  1', output)
        self.assertIn('Student names:  Alice, Charlie', output)
        self.assertIn('Student names:  Bob', output)

if __name__ == "__main__":
    unittest.main()
