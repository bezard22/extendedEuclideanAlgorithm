import unittest
from extEuclidAlgo import ExtendedEuclideanAlgorithm

# class TestEuclidAlgo(unittest.TestCase):
#     def test_1(self):
#         eea = ExtendedEuclideanAlgorithm()
#         res = eea.eea()
#         self.assertEqual(res, 3)
    
#     def test_2(self):
#         ea = EuclideanAlgorithm()
#         res = ea.gcd(301, 973)
#         self.assertEqual(res, 7)

if __name__ == "__main__":
    # unittest.main()
    eea = ExtendedEuclideanAlgorithm()
    eea.eea(999, 19)
    print(eea.r)

[999, 19, 11, 8, 3, 2, 1, 0]