import pytest
from unittest.mock import patch
from io import StringIO
from counter1 import counter


@patch('builtins.input', side_effect=['3', 'y', 'n', 'y'])
@patch('sys.stdout', new_callable=StringIO)
def test_counter_valid_inputs(mock_stdout, mock_input):
    counter()
    output = mock_stdout.getvalue().strip().split('\n')
    assert 'Students present:  2' in output
    assert 'Students absent:  1' in output


@patch('builtins.input', side_effect=['3', 'y', 'n', 'maybe'])
@patch('sys.stdout', new_callable=StringIO)
def test_counter_invalid_input(mock_stdout, mock_input):
    counter()
    output = mock_stdout.getvalue().strip().split('\n')
    assert 'Invalid input' in output
