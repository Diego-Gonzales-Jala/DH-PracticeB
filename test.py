"""
DigitalHarbor Confidential
CODE-123
(c) Copyright DH Corp. 2020
The source code for this program is not published. Copyright.

test.py
    A set of tests to validate user emails.
"""

import unittest
from util import search_email_from_users

class UserTestCases(unittest.TestCase):
    """
    This class has a set of test cases to validate user emails.
    """

    def test_search_email_on_the_second_page_of_users(self):
        """
        Test to search an email from users page and match this email.
        """
        actual_result = search_email_from_users("michael.lawson@reqres.in")
        expected_result = "michael.lawson@reqres.in"
        if actual_result != expected_result:
            raise AssertionError("Error: emails do not match: Actual '{}' and Expected '{}'"
            .format(actual_result, expected_result))
