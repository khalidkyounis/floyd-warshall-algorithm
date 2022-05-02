""" Use cProfile to get runtime statistics for the imperative version of
Floyd_warshall Algorithm """

# Import sys and os packages
# Import testing package

import os
# Import sys and os packages
import sys

SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd-Warshall function

# Import Floyd-Warshall test cases

# Import testing package
import cProfile

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")

cProfile.run("floyd_warshall(sample_3)")
