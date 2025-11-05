import pytest
import string

# We assume you have implemented these functions in checker2.py
# and wrapped your main code in an
# if __name__ == "__main__":
#    block.

from checker2 import has_punctuation, has_digit, has_letter, is_valid_username

# --- Tests for helper functions (Password) ---

@pytest.mark.parametrize("password, expected", [
    ("hello!", True),
    ("abc", False),
    ("", False)
])
def test_has_punctuation(password, expected):
    """Tests the has_punctuation function."""
    assert has_punctuation(password) == expected

@pytest.mark.parametrize("password, expected", [
    ("hello12", True),
    ("abc", False),
    ("", False)
])
def test_has_digit(password, expected):
    """Tests the has_digit function."""
    assert has_digit(password) == expected

@pytest.mark.parametrize("password, expected", [
    ("a123", True),
    ("123", False),
    ("", False)
])
def test_has_letter(password, expected):
    """Tests the has_letter function."""
    assert has_letter(password) == expected

# --- Tests for helper function (Username) ---

@pytest.mark.parametrize("username, expected", [
    ("testuser", True),
    ("user123", True),
    ("user!", True),
    ("123", True),
    ("!@#", True),
    ("", False),
    ("   ", False) # Assuming spaces don't count
])
def test_is_valid_username(username, expected):
    """
    Tests the is_valid_username function.
    The checker2.py instructions state a valid username
    has "at least one letter, number, or punctuation mark."
    """
    assert is_valid_username(username) == expected

# Note: Testing the main logic of checker2.py is difficult
# because it uses input() and getpass().
# The core password *strength* logic is tested
# in checker1_test.py and, more thoroughly, in checker3_test.py.