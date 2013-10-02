'''
Created on Oct 2, 2013

@author: andy
'''
import unittest
from pysentiment.utils import Tokenizer

class TestTokenizer(unittest.TestCase):


    def test_token(self):
        text = 'this is a wonderful gift.'
        tokenizer = Tokenizer()
        self.assertTrue(tokenizer.tokenize(text)==['wonder', 'gift'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()