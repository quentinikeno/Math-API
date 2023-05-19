import unittest
from equations import Equations

class TestEquations(unittest.TestCase):
    """Tests for the Equations class."""
    
    def test_add_default(self):
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
        
    def test_add_custom(self):
        """Test the add method with the min and max set to 2 and 3 for the first and second numbers."""
        
        result = Equations(2, 3, 2, 3).add()
        
        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 2)
        self.assertTrue(result["first"] <= 3)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 2)
        self.assertTrue(result["second"] <= 3)
        self.assertEqual(result["operation"], "+")
        self.assertEqual(result["expression"], f'{result["first"]} + {result["second"]}')
        self.assertEqual(result["answer"], result["first"] + result["second"]),