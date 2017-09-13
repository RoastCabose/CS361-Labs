#----------------------------------------------------------------------
# test_DList.py
# Tom Green, Andrew McEwen
# 08/20/2013
#----------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '..')
from DList import *

#----------------------------------------------------------------------

class DListTest(unittest.TestCase):

    #------------------------------------------------------------------

    def check_list(self, linked, lst):

        a = list(linked)
        b = lst[:]
        self.assertEqual(a, b)
        a = list(linked.reverse_iter())
        b.reverse()
        self.assertEqual(a, b)
        
    #------------------------------------------------------------------

    def test_init(self):

        a = DList()
        self.assertEqual(len(a), 0)
        a = DList([1, 2, 3, 4])
        self.assertEqual(len(a), 4)
        self.check_list(a, [1, 2, 3, 4])

    #------------------------------------------------------------------

    def test_pop(self):

        a = DList()
        for i in range(10):
            a.append(i)
        b = list(range(10))
        self.check_list(a, b)

        self.assertEqual(a.pop(), 9)
        a.append(9)

        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)
        
        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(5), b.pop(5))
        self.check_list(a, b)
        
        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)
        
        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(1), b.pop(1))
        self.check_list(a, b)

        self.assertEqual(a.pop(1), b.pop(1))
        self.check_list(a, b)

        self.assertEqual(a.pop(), b.pop())
        self.check_list(a, b)

        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

        self.assertEqual(a.pop(0), b.pop(0))
        self.check_list(a, b)

    # ------------------------------------------------------------------

    def test_remove(self):

        a = DList()
        b = []
        for i in range(10):
            a.append(i)
            b.append(i)
            
        a.remove(0)
        a.remove(5)
        a.remove(9)

        b.remove(0)
        b.remove(5)
        b.remove(9)
        
        self.assertEqual(len(a), len(b))
        self.check_list(a, b)

        self.assertRaises(ValueError, a.remove, 10)

    # ------------------------------------------------------------------

    def test_setGetDel(self):

        a = DList([0, 1, 2, 3, 4, 5])
        self.assertEqual(a[0], 0)
        self.assertEqual(a[3], 3)
        self.assertEqual(a[-1], 5)
        self.assertEqual(a[-3], 3)
        self.assertRaises(IndexError, a.__getitem__, 10)
        self.assertRaises(IndexError, a.__getitem__, -8)

        a[4] = 8
        self.assertEqual(a[4], 8)
        a[-1] = 12
        self.assertEqual(a[5], 12)
        self.assertRaises(IndexError, a.__setitem__, 10, 5)

        a = DList([0, 1, 2, 3, 4, 5])
        del a[4]
        self.assertEqual(a[4], 5)
        del a[-1]
        self.assertEqual(a.size, 4)
        self.assertRaises(IndexError, a.__delitem__, 10)

    # ------------------------------------------------------------------

    def test_insert(self):

        a = DList([0, 1, 2, 3, 4, 5])
        a.insert(3, 24)
        self.assertEqual(a[3], 24)

        a.insert(0, 10)
        self.assertEqual(a[0], 10)

        a.insert(9, 7)
        self.assertEqual(a[-1], 7)

        a.insert(20, 8)
        self.assertEqual(a[-1], 8)

        a.insert(-20, 42)
        self.assertEqual(a[0], 42)

    # ------------------------------------------------------------------

    def test_minMax(self):

        a = DList([0,1,2,3,4,5])
        self.assertEqual(max(a), 5)
        a.append(-4)
        self.assertEqual(max(a), 5)
        a.insert(3, 10)
        self.assertEqual(max(a), 10)

        a = DList([0, 1, 2, 3, 4, 5])
        self.assertEqual(min(a), 0)
        a.append(-4)
        self.assertEqual(min(a), -4)
        a.insert(3, -6)
        self.assertEqual(min(a), -6)

        a = DList()
        self.assertRaises(ValueError, min, a)
        self.assertRaises(ValueError, max, a)

    # ------------------------------------------------------------------

    def test_extend(self):

        a = DList([1, 2, 3])
        b = DList([4, 5])
        c = DList([])
        a.extend(b)
        a.extend(c)
        self.assertEqual(list(a), [1, 2, 3, 4, 5])

    # ------------------------------------------------------------------

    def test_index(self):

        a = DList([1,5,9,6,8,2,5])
        self.assertEqual(a.index(1), 0)
        self.assertEqual(a.index(5), 1)
        self.assertEqual(a.index(5, 3), 6)

        c = DList()
        self.assertRaises(IndexError, c.index, 5)

    # ------------------------------------------------------------------

    def test_count(self):

        a = DList([1, 2, 2, 2, 3, 4])
        b = a.count(2)
        self.assertEqual(b, 3)

        self.assertEqual(a.count(5), 0)

    # ------------------------------------------------------------------


#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
