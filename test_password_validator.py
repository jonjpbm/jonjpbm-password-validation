from typing import Type
import password_validator
import unittest

class Test_Password_validator(unittest.TestCase):
    """
    Test the functions in the password_validator module
    """

    def test_is_ascii(self):
        """
        Simply test if true or fales is retruned as expected
        """
        #Good ascii string
        self.assertEqual(password_validator.is_ascii('agoodstring'),True)
        #bad ascii string
        self.assertEqual(password_validator.is_ascii('строка'),False)
        #No string
        with self.assertRaises(TypeError):
            password_validator.is_ascii()

    def test_remove_non_ascii(self):
        """
        Simply tests the removal of non ascii characters function
        """
        #test if int is passed
        with self.assertRaises(TypeError):
            password_validator.remove_non_ascii(123)

        removed=password_validator.remove_non_ascii('asdf¡Hola!')
        self.assertTrue(isinstance(removed, str))


    def test_password_len(self):
        """
        docstring
        """
        self.assertEqual(password_validator.password_len(2),False)
        self.assertEqual(password_validator.password_len(64),False)


if __name__ == '__main__':
    unittest.main()
