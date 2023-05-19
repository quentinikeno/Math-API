import unittest
from equations import Equations

class TestEquations(unittest.TestCase):
    """Tests for the Equations class."""
    
    def test_add(self):
        """Test the add method with the default settings."""
        
        result = Equations().add()
        
        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 99)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 1)
        self.assertTrue(result["second"] <= 99)
        self.assertEqual(result["operation"], "+")
        self.assertEqual(result["expression"], f'{result["first"]} + {result["second"]}')
        self.assertEqual(result["answer"], result["first"] + result["second"])