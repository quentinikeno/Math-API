import unittest
from services import equations

class TestEquations(unittest.TestCase):
    """Tests for the Equations class."""
    
    def test_add_default(self):
        """Test the add method with the default settings."""
        
        result = equations.Generator().add()
        
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
        
        result = equations.Generator(2, 3, 2, 3).add()
        
        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 2)
        self.assertTrue(result["first"] <= 3)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 2)
        self.assertTrue(result["second"] <= 3)
        self.assertEqual(result["operation"], "+")
        self.assertEqual(result["expression"], f'{result["first"]} + {result["second"]}')
        self.assertEqual(result["answer"], result["first"] + result["second"]),
        
    def test_sub_default(self):
        """Test the sub method with the default settings."""
        
        result = equations.Generator().sub()

        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 99)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 1)
        self.assertTrue(result["second"] <= 99)
        self.assertEqual(result["operation"], "-")
        self.assertEqual(result["expression"], f'{result["first"]} - {result["second"]}')
        self.assertEqual(result["answer"], result["first"] - result["second"])
        
    def test_sub_negative(self):
        """Test the sub method with negative numbers."""
        
        result = equations.Generator(1, 2, 3, 4, True).sub()

        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 2)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 3)
        self.assertTrue(result["second"] <= 4)
        self.assertEqual(result["operation"], "-")
        self.assertEqual(result["expression"], f'{result["first"]} - {result["second"]}')
        self.assertEqual(result["answer"], result["first"] - result["second"])
        self.assertTrue(result["answer"] < 0)
        
    def test_mul_default(self):
        """Test the mul method with the default settings."""
        
        result = equations.Generator().mul()

        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 99)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 1)
        self.assertTrue(result["second"] <= 99)
        self.assertEqual(result["operation"], "*")
        self.assertEqual(result["expression"], f'{result["first"]} * {result["second"]}')
        self.assertEqual(result["answer"], result["first"] * result["second"])
        
    def test_mul_custom(self):
        """Test the mul method with the custom settings."""
        
        result = equations.Generator(4, 4, 5, 5).mul()

        self.assertTrue("first" in result)
        self.assertEqual(result["first"], 4)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"], 5)
        self.assertEqual(result["operation"], "*")
        self.assertEqual(result["expression"], f'{result["first"]} * {result["second"]}')
        self.assertEqual(result["answer"], 20)
        
if __name__ == '__main__':
    unittest.main()