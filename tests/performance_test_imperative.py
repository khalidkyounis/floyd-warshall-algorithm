""" Use cProfile to get runtime statistics for the imperative version of
Floyd_warshall Algorithm """

import os
# Import sys and os packages
import sys

SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd-Warshall function
from functions.floyd_warshall_imperative import floyd_warshall

# Import Floyd-Warshall test cases
from test_samples import (sample_1, sample_2)

# Import testing package
import cProfile

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")
