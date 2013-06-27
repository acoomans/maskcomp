import unittest
import os
from maskcomp.maskcomparator import compare

class TestMaskcomparator(unittest.TestCase):

	def setUp(self):
		basedir = os.path.dirname(os.path.abspath(__file__))
		self.img1 = basedir + "/images/image1.png"
		self.img2 = basedir + "/images/image2.png"
		self.mask = basedir + "/images/mask.png"

	def test_same(self):
		r = compare(
			self.img1,
			self.img1
		)
		self.assertTrue(r == 0)
		
	def test_different(self):
		r = compare(
			self.img1,
			self.img2
		)
		self.assertTrue(r > 0)
		
	def test_masked(self):
		r = compare(
			self.img1,
			self.img2,
			self.mask
		)
		self.assertTrue(r == 0)

if __name__ == '__main__':
	unittest.main()