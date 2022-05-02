""" Perform Unit Testing to test the recursive version of Floyd_warshall
Algorithm """

# Import testing package
import unittest

# Import Floyd Warshall function
from functions.floyd_warshall_recursive import floyd_warshall
# Import Floyd Warshall test cases
from tests.test_samples import (sample_1, sample_2, sample_3, result_1,
                                result_2, result_3)


# Unit Tests
class TestFloydWarshall(unittest.TestCase):
    """TestFloydWarshall class inherits the unittest module"""

    def test_floyd_warshall_1(self):
        """define test_floyd_warshall_1 function to check whether the output
        that floyd_warshall function gives is equal to result array """

        # Check whether the output of the floyd_warshall function and
        # compare it with correspondent result array in test_samples file
        self.assertEqual(floyd_warshall(sample_1), result_1,
                         "Output incorrect")

    def test_floyd_warshall_2(self):
        """define test_floyd_warshall_2 function to check whether the output
        that floyd_warshall function gives is equal to result array """

        # Check whether the output of the floyd_warshall function and
        # compare it with correspondent result array in test_samples file
        self.assertEqual(floyd_warshall(sample_2), result_2,
                         "Output incorrect")

    def test_floyd_warshall_3(self):
        """define test_floyd_warshall_2 function to check whether the output
        that floyd_warshall function gives is equal to result array """

        # Check whether the output of the floyd_warshall function and
        # compare it with correspondent result array in test_samples file
        self.assertEqual(floyd_warshall(sample_3), result_3,
                         "Output incorrect")


if __name__ == '__main__':
    # Run the testing script
    unittest.main()
