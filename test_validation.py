
import unittest
from validation import validate_age, validate_username


class TestValidation(unittest.TestCase):

    def test_valid_age(self):
        self.assertEqual(validate_age(25), 25)
        self.assertEqual(validate_age("30"), 30)
        self.assertEqual(validate_age(0), 0)
        self.assertEqual(validate_age(120), 120)

    def test_missing_age(self):
        with self.assertRaisesRegex(ValueError, "Age is required"):
            validate_age(None)

    def test_invalid_age_range(self):
        for age in [-1, 121]:
            with self.subTest(age=age):
                with self.assertRaises(ValueError):
                    validate_age(age)

    def test_invalid_age_format(self):
        with self.assertRaises(ValueError):
            validate_age("abc")

    def test_valid_username(self):
        self.assertEqual(validate_username("john"), "john")
        self.assertEqual(validate_username("  alice  "), "alice")

    def test_missing_username(self):
        with self.assertRaisesRegex(ValueError, "Username is required"):
            validate_username("")

        with self.assertRaises(ValueError):
            validate_username(None)


if __name__ == "__main__":
    unittest.main()

