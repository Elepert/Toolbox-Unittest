'''
Unittest toolbox code below
'''
import unittest
from unittest import TestCase

class TestStringMethods(unittest.TestCase):

    def test_remove_negative(self):
        self.assertEqual(self.remove_negative([-1,2,3,4,-6,-7,-8]), [2,3,4])


        self.assertEqual(self.remove_negative([2,3,4,4,5]), [2,3,4,4,5])
        self.assertEqual(self.remove_negative([-1,-6,-7,-8]), [])

    def remove_negative(self, negative_list):
    	negative_list.sort()
    	positive_list = [x for x in negative_list if x >= 0 ]
    	return(positive_list)

if __name__ == '__main__':
    unittest.main(verbosity = 2)

