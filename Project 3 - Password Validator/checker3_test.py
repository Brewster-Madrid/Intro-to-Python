import pytest

# This test file is for Exercise 3: Breaking the code.
# It runs tests against the logic in checker2.py.

# To make this work, you must have refactored your
# strength-checking logic in checker2.py into a testable function.
# We will assume it is named 'check_strength'.

from checker2 import check_strength

@pytest.mark.parametrize("password, expected_strength", [
    # --- Defined Cases (from checker1/2) ---
    ("pass", "short"),
    ("abcdefghi", "weak"),
    ("abcdefg123", "medium"),
    ("Pass123!", "strong"),
    ("", "short"),

    # --- Edge Cases (The "Breaking" part from checker3) ---
    # These are cases the original instructions didn't describe.
    # A simple program might crash (return None) or misclassify them.
    # Your goal is to update checker2.py to pass these tests.
    
    # Just numbers (long enough)
    ("123456789", "weak"),
    
    # Just punctuation (long enough)
    ("!@#$%^&*", "weak"),
    
    # Letters and Punctuation (no numbers)
    ("abcdefg!@#", "medium"),
    
    # Numbers and Punctuation (no letters)
    ("1234567!@#", "medium"),
    
    # Whitespace only (long enough)
    ("         ", "weak"),
])
def test_strength_edge_cases(password, expected_strength):
    """
    Tests the check_strength function for undefined or ambiguous cases.
    
    This test makes assumptions about what strength *should* be.
    For example, we assume "just numbers" is "weak" and
    "letters + punctuation" is "medium".
    
    Your goal is to update your check_strength function in checker2.py
    to correctly handle all these cases and pass this test.
    """
    assert check_strength(password) == expected_strength

def test_unhandled_cases_do_not_crash():
    """
    Checks that unhandled cases at least return a string
    and not 'None' (which can happen with if/elif
    without a final 'else').
    """
    unhandled_passwords = [
        "123456789",
        "!!!!!!!!!",
        "abcdefg!@#",
        "1234567!@#",
        "         ",
    ]
    
    for password in unhandled_passwords:
        strength = check_strength(password)
        assert strength is not None, f"check_strength() returned None for '{password}'"
        assert isinstance(strength, str), f"check_strength() did not return a string for '{password}'"