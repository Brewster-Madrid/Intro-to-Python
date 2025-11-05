import pytest
from unittest.mock import patch
from io import StringIO

from counter2 import counter


@patch('builtins.input', side_effect=['3', 'Alice', 'Bob', 'Charlie', 'y', 'y', 'n', 'y'])
@patch('sys.stdout', new_callable=StringIO)
def test_counter(mock_stdout, mock_input):
    counter()
    output = mock_stdout.getvalue()
    
    assert 'Students present:  2' in output
    assert 'Students absent:  1' in output
    assert 'Student names:  Alice, Charlie' in output
    assert 'Student names:  Bob' in output
