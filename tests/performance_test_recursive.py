""" Use cProfile to get runtime statistics for the recursive version of
Floyd_warshall Algorithm """

# Import built-in packages
import cProfile
import sys

# This is used because the function file is not in the path where recursive
# and imperative functions are so when searching from tests folder it looks
# only for files in same directory as it


sys.path.append('.')

# Import Floyd Warshall function
from functions.floyd_warshall_recursive import floyd_warshall
# Import Floyd Warshall test cases
from tests.test_samples import (sample_1, sample_2, sample_3, result_1,
                                result_2, result_3)

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")

cProfile.run("floyd_warshall(sample_3)")
