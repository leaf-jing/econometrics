#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 00:37:59 2016

@author: lifujing
"""

import unittest, numpy as np, numpy.testing as npt
import logging as log
from econ import ls
import loginit

loginit.setup_logging()
logger = log.getLogger(__name__)
#test case: the individual unit of testing
#test suite: a collection of test cases, test suites, or both.
#test runner:  
class TestLsModel(unittest.TestCase):
    """
    assertEqual, assertTrue, assertFalse, 
    assertRaise(verify that a specific exception get raised) 
    setUp, tearDown: define instructions executing before/after test methods
    """
    def test_ls(self):
        # y = 0.5 + 2x
        x=np.array([[1],[2],[3]])
        y=np.array([[2.502],[4.496],[6.502]])
        model = ls.LSModel(x,y)
        # check regression
        beta = model.beta
        beta = model.beta
        npt.assert_array_almost_equal(beta, np.array([[0.5],[2]]))
        logger.info("Beta is : %s", beta)
        # check residual
        expected_residual = np.array([0.002,-0.004,0.002]).reshape(3,1)
        npt.assert_array_almost_equal(model.residauls, expected_residual)
        npt.assert_array_almost_equal(model.r_sqaure , 0.999997)
        npt.assert_array_almost_equal(model.r_sqaure_adj , 0.999994)
        
""" 
(1) discover all file match the pattern in dir/subdir of "unit_tests"        
python -m unittest discover -s unit_tests -p  "test_*.py"       
** -m mod : run library module as a script (terminates option list)

(2) run the script directly use the main entry point
"""
        
if __name__ == '__main__':
    print("Run from the main entry point...")
    unittest.main()
    