import unittest

def tinh_tong(a, b):
    return a+b +1

class TestMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(tinh_tong(3, 3), 7)

    def test2(self):
        self.assertEqual(tinh_tong(2, 6), 8)

    def test3(self):
        self.assertEqual(tinh_tong(1, 9 ), 10)

if __name__=='__main__':
    unittest.main()        