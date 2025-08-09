# test_htmlsanitizer.py
"""
Tests for HtmlSanitizer module.
"""

import unittest
from htmlsanitizer import HtmlSanitizer

class TestHtmlSanitizer(unittest.TestCase):
    """Test cases for HtmlSanitizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HtmlSanitizer()
        self.assertIsInstance(instance, HtmlSanitizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HtmlSanitizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
