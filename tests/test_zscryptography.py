import unittest
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..\zscryptography')))
from zscryptography import *

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.key = 'thisisaverysecretkey123456789012'  
        self.plain_text = "Hello, World!"
  
    def test_encrypt_decrypt(self):
        encrypted = encrypt(self.key,self.plain_text)
        decrypted = decrypt(self.key,encrypted)
        self.assertEqual(self.plain_text, decrypted)

if __name__ == '__main__':
    unittest.main()