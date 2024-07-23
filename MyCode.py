import random
import string
def generate_google_play_codes(num_codes: int) -> list:
    """
    Generates Google Play codes by randomly generating 16-character alphanumeric strings.
 
    Parameters:
    - num_codes: int
        The number of Google Play codes to generate.
 
    Returns:
    - list:
        A list of randomly generated Google Play codes.
 
    Raises:
    - ValueError:
        Raises an error if the number of codes requested is less than or equal to zero.
    """
 
    if num_codes <= 0:
        raise ValueError("Number of codes should be greater than zero.")
 
    google_play_codes = []
 
    for _ in range(num_codes):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        formatted_code = '-'.join([code[i:i+4] for i in range(0, 16, 4)])
        google_play_codes.append(formatted_code)
 
    return google_play_codes
 
# Unit tests for generate_google_play_codes function.
 
import unittest
 
class TestGenerateGooglePlayCodes(unittest.TestCase):
 
    def test_generate_single_code(self):
        """
        Tests generating a single Google Play code.
        """
        codes = generate_google_play_codes(1)
        self.assertEqual(len(codes), 1)
        self.assertEqual(len(codes[0]), 19)
        self.assertEqual(codes[0].count('-'), 3)
 
    def test_generate_multiple_codes(self):
        """
        Tests generating multiple Google Play codes.
        """
        codes = generate_google_play_codes(5)
        self.assertEqual(len(codes), 5)
        for code in codes:
            self.assertEqual(len(code), 19)
            self.assertEqual(code.count('-'), 3)
 
    def test_generate_zero_codes(self):
        """
        Tests generating zero Google Play codes.
        """
        with self.assertRaises(ValueError):
            generate_google_play_codes(0)
 
    def test_generate_negative_codes(self):
        """
        Tests generating negative number of Google Play codes.
        """
        with self.assertRaises(ValueError):
            generate_google_play_codes(-5)
 
# Example usage of generate_google_play_codes function:
 
num_codes = int(input("How many Google Play codes do you want to generate? "))
codes = generate_google_play_codes(num_codes)
print("Generated Google Play codes:")
for code in codes:
    print(code)
    