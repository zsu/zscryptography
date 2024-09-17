import unittest
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\zscryptography')))
from zscryptography import encrypt, decrypt  # Import from local zscryptography.py

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.key = 'thisisaverysecretkey123456789012'  
        self.iv = 'thisisasecretiv1'
        self.plain_text = "Hello, World!"

    def test_encrypt_decrypt_with_iv(self):
        encrypted = encrypt(self.plain_text, self.key, self.iv)
        decrypted = decrypt(encrypted, self.key, self.iv)
        self.assertEqual(self.plain_text, decrypted)

    def test_encrypt_decrypt_without_iv(self):
        encrypted = encrypt(self.plain_text, self.key)
        decrypted = decrypt(encrypted, self.key)
        self.assertEqual(self.plain_text, decrypted)

if __name__ == '__main__':
    unittest.main()