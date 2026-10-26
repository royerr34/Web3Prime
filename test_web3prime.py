# test_web3prime.py
"""
Tests for Web3Prime module.
"""

import unittest
from web3prime import Web3Prime

class TestWeb3Prime(unittest.TestCase):
    """Test cases for Web3Prime class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Prime()
        self.assertIsInstance(instance, Web3Prime)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Prime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
