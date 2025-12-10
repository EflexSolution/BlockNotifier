# test_blocknotifier.py
"""
Tests for BlockNotifier module.
"""

import unittest
from blocknotifier import BlockNotifier

class TestBlockNotifier(unittest.TestCase):
    """Test cases for BlockNotifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockNotifier()
        self.assertIsInstance(instance, BlockNotifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockNotifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
