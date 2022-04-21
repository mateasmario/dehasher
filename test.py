import unittest
import utils.Hashing
import utils.Multiprocessing

class TestHash(unittest.TestCase):
    def test_md5(self):
        self.assertEqual(utils.Hashing.Hash("MD5", "Hello, world!"), "6cd3556deb0da54bca060b4c39479839", "MD5 encryption failed.")
    def test_sha1(self):
        self.assertEqual(utils.Hashing.Hash("SHA1", "Hello, world!"), "943a702d06f34599aee1f8da8ef9f7296031d699", "SHA1 encryption failed.")
    def test_sha224(self):
        self.assertEqual(utils.Hashing.Hash("SHA224", "Hello, world!"), "8552d8b7a7dc5476cb9e25dee69a8091290764b7f2a64fe6e78e9568", "SHA224 encryption failed.")
    def test_sha256(self):
        self.assertEqual(utils.Hashing.Hash("SHA256", "Hello, world!"), "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3", "SHA256 encryption failed.")
    def test_sha384(self):
        self.assertEqual(utils.Hashing.Hash("SHA384", "Hello, world!"), "55bc556b0d2fe0fce582ba5fe07baafff035653638c7ac0d5494c2a64c0bea1cc57331c7c12a45cdbca7f4c34a089eeb", "SHA384 encryption failed.")
    def test_sha512(self):
        self.assertEqual(utils.Hashing.Hash("SHA512", "Hello, world!"), "c1527cd893c124773d811911970c8fe6e857d6df5dc9226bd8a160614c0cd963a4ddea2b94bb7d36021ef9d865d5cea294a82dd49a0bb269f51f6e7a57f79421", "SHA512 encryption failed.")

class TestIdentifyHashMethod(unittest.TestCase):
    def test_existing(self):
        self.assertEqual(utils.Hashing.Identify("6cd3556deb0da54bca060b4c39479839"), "MD5", "MD5 identification failed.")
        self.assertEqual(utils.Hashing.Identify("943a702d06f34599aee1f8da8ef9f7296031d699"), "SHA1", "SHA1 identification failed.")
        self.assertEqual(utils.Hashing.Identify("8552d8b7a7dc5476cb9e25dee69a8091290764b7f2a64fe6e78e9568"), "SHA224", "SHA224 identification failed.")
        self.assertEqual(utils.Hashing.Identify("315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3"), "SHA256", "SHA256 identification failed.")
        self.assertEqual(utils.Hashing.Identify("55bc556b0d2fe0fce582ba5fe07baafff035653638c7ac0d5494c2a64c0bea1cc57331c7c12a45cdbca7f4c34a089eeb"), "SHA384", "SHA384 identification failed.")
        self.assertEqual(utils.Hashing.Identify("c1527cd893c124773d811911970c8fe6e857d6df5dc9226bd8a160614c0cd963a4ddea2b94bb7d36021ef9d865d5cea294a82dd49a0bb269f51f6e7a57f79421"), "SHA512", "SHA512 identification failed.")
    def test_notExisting(self):
        self.assertEqual(utils.Hashing.Identify("####"), None, "Unidentified hash returning None failed.")

class TestDehashing(unittest.TestCase):
    def test_md5(self):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+{}[]:\";'|\\<>,.?/~ "
        self.assertEqual(utils.Hashing.Generate("MD5", "0cc175b9c0f1b6a831c399e269772661", 1, chars), True) # string 'a'
        self.assertEqual(utils.Hashing.Generate("MD5", "a8ae67a7d91a310d67c643a73cb9d031", 3, chars), True) # string 'edd'
        self.assertEqual(utils.Hashing.Generate("MD5", "900150983cd24fb0d6963f7d28e17f72", 2, chars), False) # string "abc"

if __name__ == "__main__":
    unittest.main()
