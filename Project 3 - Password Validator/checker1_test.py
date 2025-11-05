import pytest
import string

# We assume you have implemented these functions in checker1.py
# as described in the instructions.

# Note: To make testing work, your checker1.py file should NOT
# automatically run input() when it is imported.
# Wrap your main code (that calls input()) at the bottom
# of your file like this:
#
# if __name__ == "__main__":
#    main()  # Or whatever your main function is called

# We import the functions you were asked to write.
# If checker1.py is not yet implemented, these tests will fail.
from checker1 import has_punctuation, has_digit, has_letter

# We also import the main logic function. The instructions imply
# this logic is in the main function, but to test it,
# you must put it in its *own* function.
# We will assume it's called 'check_strength'.
from checker1 import check_strength

# --- Tests for helper functions ---

@pytest.mark.parametrize("password, expected", [
    ("hello!", True),
    ("world@", True),
    ("test#", True),
    ("abc", False),
    ("123", False),
    ("", False),
    (string.punctuation, True)
])
def test_has_punctuation(password, expected):
    """Tests the has_punctuation function."""
    assert has_punctuation(password) == expected

@pytest.mark.parametrize("password, expected", [
    ("hello12", True),
    ("456world", True),
    ("abc", False),
    ("!@#", False),
    ("", False),
    ("0", True)
])
def test_has_digit(password, expected):
    """Tests the has_digit function."""
    assert has_digit(password) == expected

@pytest.mark.parametrize("password, expected", [
    ("a123", True),
    ("Hello!", True),
    ("123", False),
    ("!@#", False),
    ("", False),
    ("Z", True)
])
def test_has_letter(password, expected):
    """Tests the has_letter function."""
    assert has_letter(password) == expected

# --- Tests for main logic ---
# This assumes you have a function 'check_strength(password)'
# that returns a string (e.g., "short", "weak", "medium", "strong").

@pytest.mark.parametrize("password, strength", [
    ("short", "short"),      # Less than or equal to 6
    ("123456", "short"),
    ("", "short"),
    ("abcdefg", "weak"),      # Letters only
    ("Password", "weak"),
    ("abcdefg123", "medium"), # Letters and numbers
    ("Pass123", "medium"),
    ("abcdefg123!", "strong"),# All three
    ("Pass123!", "strong"),
])
def test_check_strength_defined_cases(password, strength):
    """Tests the main password strength logic for defined cases."""
    assert check_strength(password) == strength