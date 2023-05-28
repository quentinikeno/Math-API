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
        
    def test_find_divisors_of_30(self):
        """Test the find_divisors on finding the divisors of 30."""
        divisors = equations.Generator(30, 30).find_divisors()
        expected_divisors = [1, 30, 2, 15, 3, 10, 5, 6]
        self.assertTrue(all(item in divisors for item in expected_divisors))
        self.assertTrue(all(item in expected_divisors for item in divisors))
        
    def test_find_divisors_of_negative_30(self):
        """Test the find_divisors on finding the divisors of -30."""
        divisors = equations.Generator(-30, -30).find_divisors()
        expected_divisors = [1, 30, 2, 15, 3, 10, 5, 6, -1, -30, -2, -15, -3, -10, -5, -6]
        self.assertTrue(all(item in divisors for item in expected_divisors))
        self.assertTrue(all(item in expected_divisors for item in divisors))
        
    def test_find_divisors_of_36(self):
        """Test the find_divisors on finding the divisors of 36."""
        divisors = equations.Generator(36, 36).find_divisors()
        expected_divisors = [1, 36, 2, 18, 3, 12, 4, 9, 6]
        self.assertTrue(all(item in divisors for item in expected_divisors))
        self.assertTrue(all(item in expected_divisors for item in divisors))
        
    def test_find_divisors_of_negative_36(self):
        """Test the find_divisors on finding the divisors of 36."""
        divisors = equations.Generator(-36, -36).find_divisors()
        expected_divisors = [1, 36, 2, 18, 3, 12, 4, 9, 6, -1, -36, -2, -18, -3, -12, -4, -9, -6]
        self.assertTrue(all(item in divisors for item in expected_divisors))
        self.assertTrue(all(item in expected_divisors for item in divisors))
        
    def test_divisors_of_0(self):
        """Test that find divisors will raise an exception when the first number is 0."""
        with self.assertRaises(ValueError):
            equations.Generator(0, 0).find_divisors()
            
    def test_div_default(self):
        """Test the div method with the default settings."""
        
        result = equations.Generator().div()

        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 99)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] >= 1)
        self.assertTrue(result["second"] <= 99)
        self.assertEqual(result["operation"], "/")
        self.assertEqual(result["expression"], f'{result["first"]} / {result["second"]}')
        self.assertEqual(result["answer"], result["first"] / result["second"])
        
    def test_div_custom(self):
        """Test the div method with the custom settings.  Check that a new divisor is found if the second number doesn't divide the first evenly."""
        
        result = equations.Generator(20, 20, 19, 19).div()

        self.assertTrue("first" in result)
        self.assertTrue("second" in result)
        self.assertTrue(result["second"] != 19)
        self.assertEqual(result["first"] % result["second"], 0)
        self.assertEqual(result["answer"], result["first"] / result["second"])
        self.assertIs(type(result["answer"]), int)
        
    def test_div_default(self):
        """Test the div method with 0 set the the first number.  The first number should be randomized so that we avoid division by 0."""
        
        result = equations.Generator(0, 0).div()

        self.assertTrue("first" in result)
        self.assertTrue(result["first"] >= 1)
        self.assertTrue(result["first"] <= 99)
        
if __name__ == '__main__':
    unittest.main()