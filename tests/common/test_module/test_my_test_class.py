import unittest

# Adjust the import path based on the new location
# Remove my_test_function as it's now a method
from src.common.test_module.my_test_class import MyTestClass


class TestMyTestClass(unittest.TestCase):
    """Tests for the MyTestClass class and its methods."""

    def setUp(self) -> None:
        """Set up a common instance for test methods."""
        self.test_value = "hello"
        self.instance = MyTestClass(test_attribute=self.test_value)

    def test_my_test_class_creation(self) -> None:
        """Test that MyTestClass can be instantiated correctly."""
        self.assertIsInstance(self.instance, MyTestClass)
        self.assertEqual(self.instance.test_attribute, self.test_value)

    def test_my_test_method_returns_true(self) -> None:
        """Test that the my_test_function method returns True."""
        self.assertTrue(self.instance.my_test_function())


if __name__ == "__main__":
    unittest.main()
