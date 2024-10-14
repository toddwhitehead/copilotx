import re

class Validator:
    def __init__(self):
        self.email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'
        self.phone_regex = r'^(\+)?1?\d{9,15}$'
        self.strong_password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    def is_valid_email(self, email):
        return self.check_valid(email, self.email_regex)

    def is_valid_phone(self, phone):
        return self.check_valid(phone, self.phone_regex)

    def is_valid_password(self, password):
        return self.check_valid(password, self.strong_password_regex)

    def check_valid(self, text, regex):
        return bool(re.search(regex, text))

# Regular expression for validating an email address
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for validating a phone number
phone_regex = r'^(\+)?1?\d{9,15}$'

# Regular expression for validating a strong password
# Must contain at least one lowercase letter, one uppercase letter, one digit, and one special character
# Length must be at least 8 characters
strong_password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

def check_valid(text, regex):
    """
    Checks if the given text matches the provided regex pattern.

    Parameters:
    - text (str): The text to validate.
    - regex (str): The regex pattern to match against.

    Returns:
    - bool: True if the text matches the regex pattern, False otherwise.
    """
    return bool(re.search(regex, text))

if __name__ == '__main__':
    # Test the validation functions with empty strings
    email_validity = "valid" if check_valid('', email_regex) else "invalid"
    phone_validity = "valid" if check_valid('', phone_regex) else "invalid"
    password_validity = "valid" if check_valid('', strong_password_regex) else "invalid"

    print(f"Email is {email_validity}")
    print(f"Phone number is {phone_validity}")
    print(f"Password is {password_validity}")

# Example usage with a testing framework like unittest

import unittest

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_email_validation(self):
        self.assertTrue(self.validator.is_valid_email("test@example.com"))
        self.assertFalse(self.validator.is_valid_email("test@example"))

    def test_phone_validation(self):
        self.assertTrue(self.validator.is_valid_phone("+12345678901"))
        self.assertFalse(self.validator.is_valid_phone("12345"))

    def test_password_validation(self):
        self.assertTrue(self.validator.is_valid_password("StrongPass1!"))
        self.assertFalse(self.validator.is_valid_password("weak"))

if __name__ == '__main__':
    unittest.main()


