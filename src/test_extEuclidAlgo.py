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
    print(eea.eea(243, 198))
    # print(eea.eea(3587, 1819))
    print(eea.formatExplanation())