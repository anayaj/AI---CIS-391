import unittest
from homework9 import *
import os
from os import listdir

class MyTests(unittest.TestCase):

	def test1(self):
		train = [({"x1":1}, True), ({"x2":1}, True), ({"x1": -1}, False),({"x2": -1}, False)]
		test = [{"x1":1}, {"x1":1, "x2":1}, {"x1": -1, "x2":1.5},{"x1": -0.5, "x2": -2}]

		# Train the classifier for one iteration
		p = BinaryPerceptron(train,1)

		# Make predictions on the test data
		self.assertEqual([p.predict(x) for x in test], [True, True, True, False])

	def test2(self):
		train = [({"x1":1},1), ({"x1":1, "x2":1},2), ({"x2":1},3),({"x1": -1, "x2":1},4), ({"x1": -1},5), ({"x1": -1, "x2": -1},6),({"x2": -1},7), ({"x1":1, "x2": -1},8)]

		# Train the classifier for10 iterations so that it can learn each class
		p = MulticlassPerceptron(train,10)

		# Test whether the classifier correctly learned the training data
		self.assertEqual([p.predict(x) for x, y in train], [1,2,3,4,5,6,7,8])

	def test3(self):
		c = IrisClassifier(data.iris)
		self.assertEqual(c.classify((5.1,3.5,1.4,0.2)),'iris-setosa');
		self.assertEqual(c.classify((7.0,3.2,4.7,1.4)),'iris-versicolor');

	def test4(self):
		c = BiasClassifier(data.bias)
		self.assertEqual([c.classify(x) for x in (-1, 0, 0.5, 1.5, 2)],[False, False, False, True, True]);

	def test5(self):
		c = MysteryClassifier1(data.mystery1)
		self.assertEqual([c.classify(x) for x in ((0, 0), (0, 1), (-1, 0), (1, 2), (-3, -4))],[False, False, False, True, True]);

	def test6(self):
		c = MysteryClassifier2(data.mystery2)
		self.assertEqual([c.classify(x) for x in ((1, 1, 1), (-1, -1, -1), (1, 2, -3), (-1, -2, 3))],[True, False, False, True]);

	def test7(self):
		c = DigitClassifier(data.digits)
		self.assertEqual(c.classify((0,0,5,13,9,1,0,0,0,0,13,15,10,15,5,0,0,3,15,2,0,11,8,0,0,4,12,0,0,8,8,0,0,5,8,0,0,9,8,0,0,4,11,0,1,12,7,0,0,2,14,5,10,12,0,0,0,0,6,13,10,0,0,0)),0);
		self.assertEqual(c.classify((0,0,7,11,15,6,0,0,0,3,16,15,12,4,0,0,0,5,16,13,14,8,0,0,0,6,15,11,8,15,6,0,0,0,0,0,0,8,8,0,0,0,0,0,0,4,8,0,0,0,13,9,8,13,5,0,0,0,6,11,14,9,0,0)),5);
		self.assertEqual(c.classify(( 0, 0, 7,16,15, 5, 0, 0, 0, 0,15, 7, 6,15, 2, 0, 0, 3,15, 4, 5,13, 2, 0, 0, 2,15,16,16,15, 0, 0, 0, 0, 8,16,15,15, 3, 0, 0, 0,11,13, 1, 6, 7, 0, 0, 0,16,12, 8,11, 4, 0, 0, 0, 7,15,16,12, 2, 0)), 8);
		self.assertEqual(c.classify(( 0, 0, 5,12,12, 0, 0, 0, 0, 3,16,12,15, 4, 0, 0, 0, 4,14, 0,14, 6, 0, 0, 0, 1,12,11,12, 0, 0, 0, 0, 0, 7,16, 8, 1, 0, 0, 0, 0, 1, 5,12,13, 1, 0, 0, 0, 8, 4, 0,16, 4, 0, 0, 0, 8,15,15,11, 1, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 5,15, 8, 0, 0, 0, 0, 2,15, 9,10, 3, 1, 0, 0, 6, 9, 7,11,14, 1, 0, 0, 2,15,13, 8, 2, 0, 0, 0, 1,15, 6, 0, 0, 0, 0, 0, 1,16,12, 0, 0, 0, 0, 0, 1,16,13, 1, 0, 0, 0, 0, 0, 8,15, 3, 0, 0, 0)), 8);
		self.assertEqual(c.classify(( 0, 0, 9,13, 4, 0, 0, 0, 0, 1,16, 9,11, 0, 0, 0, 0, 2,11, 0,13, 0, 0, 0, 0, 0, 2, 3,13, 0, 0, 0, 0, 0, 0,11, 5, 0, 0, 0, 0, 0, 3,14, 1, 0, 0, 0, 0, 0,11,14,10, 8,11, 0, 0, 0,11,13,12,12,14, 2)), 2);
		self.assertEqual(c.classify(( 0, 0, 0, 0,13,12, 1, 0, 0, 0, 0, 5,16,16, 1, 0, 0, 0, 0,14,16,14, 0, 0, 0, 0, 7,16,16,10, 0, 0, 0, 5,16,16,16,14, 0, 0, 0, 2, 6, 9,16,16, 1, 0, 0, 0, 0, 2,16,16, 7, 0, 0, 0, 0, 0, 8,12, 6, 0)), 1);
		self.assertEqual(c.classify(( 0, 0, 2,13,15, 1, 0, 0, 0, 2,13,15, 5, 9, 0, 0, 0, 7,15, 2, 0, 8, 0, 0, 0, 8,15, 0, 0, 5, 4, 0, 0, 7,16, 0, 0, 9, 6, 0, 0, 0,14, 7, 0,13, 7, 0, 0, 0,10,15,14,14, 0, 0, 0, 0, 0,14,14, 5, 0, 0)), 0);
		self.assertEqual(c.classify(( 0, 0, 5,15,13, 2, 0, 0, 0, 0,10,13,12,11, 0, 0, 0, 0, 3, 2, 4,15, 0, 0, 0, 0, 0, 9,16,10, 0, 0, 0, 0, 0, 3,13,16, 6, 0, 0, 0, 0, 0, 0, 7,14, 0, 0, 0, 5, 8, 8,10,16, 1, 0, 0, 4, 9,14,13, 7, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 3,12,13, 9, 0, 0, 0, 0,12, 8, 2,12, 2, 0, 0, 0,11, 8,12,11, 0, 0, 0, 0, 7,16, 5, 0, 0, 0, 0, 3,12, 6,11, 0, 0, 0, 0, 4, 8, 0, 7, 9, 0, 0, 0, 1,12, 2, 0,13, 4, 0, 0, 0, 2,12,11,12, 6, 0)), 8);
		self.assertEqual(c.classify(( 0, 0, 3,13,13, 2, 0, 0, 0, 4,16,15,14,10, 0, 0, 0, 3,16, 2, 0,16, 4, 0, 0, 6,13, 0, 0,13, 6, 0, 0, 4,13, 0, 0,11, 9, 0, 0, 0,16, 0, 0,11, 7, 0, 0, 0, 9,12, 9,15, 2, 0, 0, 0, 2,11,15, 7, 0, 0)), 0);
		self.assertEqual(c.classify(( 0, 0, 3,14, 8, 0, 0, 0, 0, 8,16,16,16, 6, 0, 0, 0,11,14, 4, 7,14, 0, 0, 0, 9,10, 0, 0,12, 7, 0, 0, 6,11, 0, 0, 6, 8, 0, 0, 0,16, 4, 0, 4,12, 0, 0, 0,10,14,10,14,10, 0, 0, 0, 2,12,16,13, 2, 0)), 0);
		self.assertEqual(c.classify(( 0, 6,16,16,13, 3, 0, 0, 0,12,16,12,15,16, 5, 0, 0,10,14, 1, 0, 4, 1, 0, 0, 2,15, 8, 0, 0, 0, 0, 0, 0, 7,16, 2, 0, 0, 0, 0, 0, 2,15, 9, 0, 0, 0, 0, 1, 5,15,10, 0, 0, 0, 0, 7,16,15, 1, 0, 0, 0)), 5);
		self.assertEqual(c.classify(( 0, 2,13,16,16,11, 0, 0, 0, 7,13, 4,11,14, 0, 0, 0, 0, 1, 9,16, 7, 0, 0, 0, 0, 7,16,14, 1, 0, 0, 0, 0, 0, 9,15,13, 1, 0, 0, 0, 0, 0, 3,16, 5, 0, 0, 0, 6, 0, 5,15, 7, 0, 0, 0,15,16,16,10, 1, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 4,11,15, 4, 0, 0, 0, 3,15,15,10,16, 0, 0, 0, 8,15, 2, 0,14, 4, 0, 0, 7,13, 0, 0,10, 8, 0, 0, 7,12, 0, 0,13, 4, 0, 0, 1,15, 4, 1,15, 2, 0, 0, 0,10,12,11,12, 0, 0, 0, 0, 2,11,13, 2, 0, 0)), 0);
		self.assertEqual(c.classify(( 0, 0, 0, 2,14, 1, 0, 0, 0, 0, 0,10,12, 0, 0, 0, 0, 0, 8,15, 1, 2, 1, 0, 0, 3,15, 5, 0,12, 7, 0, 0,10,14, 0, 6,16, 2, 0, 0, 8,16,16,16,12, 0, 0, 0, 0, 2, 4,16, 5, 0, 0, 0, 0, 0, 2,13, 0, 0, 0)), 4);
		self.assertEqual(c.classify(( 0, 1,13,16, 7, 0, 0, 0, 0, 8,15,15, 9, 0, 0, 0, 0,12, 8, 8,12, 0, 0, 0, 0,10, 7, 8,12, 0, 0, 0, 0, 1, 0,11,10, 0, 0, 0, 0, 0, 3,16, 5, 0, 0, 0, 0, 0,13,15, 6, 6, 1, 0, 0, 1,16,16,16,16, 8, 0)), 2);
		self.assertEqual(c.classify(( 0, 0, 0,15,12, 5, 0, 0, 0, 0, 4,16,16, 8, 0, 0, 0, 0, 9,16,15, 3, 0, 0, 0, 1,16,16, 9, 0, 0, 0, 0, 6,16,16, 9, 0, 0, 0, 0, 0,11,16,11, 0, 0, 0, 0, 0, 4,16,14, 1, 0, 0, 0, 0, 0,13,16, 0, 0, 0)), 1);
		self.assertEqual(c.classify(( 0, 0, 9,14, 0, 0, 0, 0, 0, 4,16, 8, 0, 0, 0, 0, 0, 7,14, 1, 0, 0, 0, 0, 0, 9,11, 0, 4, 5, 1, 0, 0, 9,12,13,16,16,11, 0, 0, 4,16,15, 8,11,14, 0, 0, 3,16,11, 9,16, 6, 0, 0, 0, 8,16,16, 8, 0, 0)), 6);
		self.assertEqual(c.classify(( 0, 0, 1, 9,14, 5, 0, 0, 0, 0, 8,15, 9,14, 1, 0, 0, 0, 3,14, 0,16, 4, 0, 0, 0, 0, 8,14,16, 4, 0, 0, 0, 0, 0, 3,13, 5, 0, 0, 0, 3, 0, 0, 8, 7, 0, 0, 3,15, 6, 2,14, 6, 0, 0, 0, 1,10,14,14, 1, 0)), 9);
		self.assertEqual(c.classify(( 0, 0, 0, 1,15, 3, 0, 0, 0, 0, 1,11,11, 1, 0, 0, 0, 0,10,13, 0,10, 0, 0, 0, 6,16, 6, 6,15, 3, 0, 0, 8,16,16,16,16, 9, 0, 0, 0, 2, 4,15, 4, 0, 0, 0, 0, 0, 1,16, 1, 0, 0, 0, 0, 0, 2,15, 0, 0, 0)), 4);
		self.assertEqual(c.classify(( 0, 0, 0, 9,15, 7, 0, 0, 0, 0, 7,16,10, 6, 0, 0, 0, 0,14, 8, 0, 0, 0, 0, 0, 1,16, 5,11, 8, 0, 0, 0, 3,16,16,10,15, 9, 0, 0, 1,15, 9, 0, 4,13, 0, 0, 0,11,14, 6,11,15, 0, 0, 0, 0,10,14,13, 8, 0)), 6);
		self.assertEqual(c.classify(( 0, 0, 1, 9,13, 1, 0, 0, 0, 0,11,11,13, 9, 0, 0, 0, 2,15, 0, 4,16, 4, 0, 0, 8, 9, 0, 0,13, 6, 0, 0, 5,12, 0, 0, 9, 8, 0, 0, 0,15, 3, 0, 8, 8, 0, 0, 0, 6,14, 4,11, 7, 0, 0, 0, 0,11,16,13, 2, 0)), 0);
		self.assertEqual(c.classify(( 0, 0,11,15, 7, 0, 0, 0, 0, 2,16,10,16,14, 4, 0, 0, 5,13, 0, 6,16, 6, 0, 0, 4,16, 9,10,16, 8, 0, 0, 0, 7,12,11,14, 8, 0, 0, 0, 0, 0, 0,12, 8, 0, 0, 1,12,10,10,15, 6, 0, 0, 1,10,12,14,10, 1, 0)), 9);
		self.assertEqual(c.classify(( 0, 0, 5,16,10, 1, 0, 0, 0,11,14,13,14,12, 0, 0, 0,12,16, 4, 3,15, 5, 0, 0,11,12, 1, 0, 7, 9, 0, 0, 9,10, 0, 0, 3,14, 0, 0, 6,14, 0, 0, 9,16, 0, 0, 0,14, 9, 9,16,11, 0, 0, 0, 5,15,16,15, 1, 0)), 0);
		self.assertEqual(c.classify(( 0, 0, 6,14,16,13, 0, 0, 0, 6,14, 3, 0,13, 4, 0, 0, 5,12, 0, 4,16, 3, 0, 0, 0,14,14,15, 5, 0, 0, 0, 1,14,12, 1, 0, 0, 0, 0, 5,16,13, 2, 0, 0, 0, 0, 2,16,16,13, 0, 0, 0, 0, 0, 2,12,12, 0, 0, 0)), 8);
		self.assertEqual(c.classify(( 0, 0, 1, 7,12, 5, 0, 0, 0, 0, 4,16, 9, 6, 0, 0, 0, 0,11, 8, 0, 0, 0, 0, 0, 0,15, 8, 8, 5, 0, 0, 0, 0,16,16,12,16, 2, 0, 0, 0,15, 5, 0,15, 5, 0, 0, 0,11, 9, 8,16, 4, 0, 0, 0, 2,14,15, 8, 0, 0)), 6);
		self.assertEqual(c.classify(( 0, 0, 7,16, 4, 0, 0, 0, 0, 0, 9,16, 6, 0, 0, 0, 0, 1,13,16, 6, 0, 0, 0, 0, 9,16,16,11, 0, 0, 0, 0, 8, 6,10,16, 1, 0, 0, 0, 0, 0, 2,16,11, 0, 0, 0, 0, 1, 7,16,16, 7, 0, 0, 0, 4,15,16,15,15, 3)), 1);
		self.assertEqual(c.classify(( 0, 0, 0, 8,15, 5, 0, 0, 0, 0, 0,15,16,11, 0, 0, 0, 0, 8,16,16,13, 0, 0, 0, 7,16,16,16,16, 4, 0, 0, 2, 4, 0,10,16,10, 0, 0, 0, 0, 0, 8,16,11, 0, 0, 0, 0, 7,14,16,10, 0, 0, 0, 0,11,16, 9, 1, 0)), 1);
		self.assertEqual(c.classify(( 0, 0,12,15, 9, 0, 0, 0, 0, 8,13,10,16, 2, 0, 0, 0, 4, 4, 0,15, 6, 0, 0, 0, 0, 0, 7,16, 9, 0, 0, 0, 0, 0, 5,10,16, 4, 0, 0, 0, 0, 0, 0, 8, 9, 0, 0, 0, 8, 5, 4, 9,12, 0, 0, 1,14,14,16,14, 3, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 8,16,13, 4, 0, 0, 0, 0, 5, 6,12,14, 0, 0, 0, 0, 0, 3,15,14, 0, 0, 0, 0, 0,13,15, 4, 0, 0, 0, 0, 0, 9,12, 1, 0, 0, 0, 0, 0, 1,11,12, 0, 0, 0, 0, 3, 4, 9,16, 4, 0, 0, 0, 8,15,14,12, 3, 0)), 3);
		self.assertEqual(c.classify(( 0, 1,10,16,13, 2, 0, 0, 0, 6,14, 9,16, 6, 0, 0, 0, 0, 1, 0,13,11, 0, 0, 0, 0, 1,13,16,11, 1, 0, 0, 0, 2,12,11,16, 8, 0, 0, 0, 5, 0, 0,15, 9, 0, 0, 3,16,12, 8,16, 7, 0, 0, 0,10,16,16,11, 1, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 3, 9,15, 8, 0, 0, 0, 1,15,16,16, 7, 0, 0, 0, 0, 5,16,16,10, 4, 0, 0, 0, 3,16,16,16, 9, 0, 0, 0, 0,15,14, 4, 0, 0, 0, 0, 0,13, 5, 0, 0, 0, 0, 0, 1,15, 3, 0, 0, 0, 0, 0, 4,13, 0, 0, 0, 0)), 7);
		self.assertEqual(c.classify(( 0, 0,14,16,16,16, 9, 0, 0, 0, 6, 8,10,16, 6, 0, 0, 0, 0, 0, 9,14, 2, 0, 0, 0,13,14,16,14, 4, 0, 0, 0, 8,16,16,16,11, 0, 0, 0, 3,16, 4, 3, 1, 0, 0, 0,11,12, 0, 0, 0, 0, 0, 0,16, 8, 0, 0, 0, 0)), 7);
		self.assertEqual(c.classify(( 0, 0,12,16,15, 6, 0, 0, 0, 0,15,13,11,16, 3, 0, 0, 0, 1, 7, 5,16, 5, 0, 0, 0, 1,13,16,11, 0, 0, 0, 0, 1,10,15,15, 1, 0, 0, 0, 0, 0, 0,13,11, 0, 0, 2,11, 4, 4,14, 8, 0, 0, 0,11,16,16,14, 1, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 3,16,13, 2, 0, 0, 0, 0,11, 7, 7,12, 0, 0, 0, 2,16, 1, 0, 9, 3, 0, 0, 5,13, 1, 0, 6, 6, 0, 0, 7, 6, 0, 0, 5, 8, 0, 0, 4, 8, 0, 0,10, 5, 0, 0, 1,13, 5, 8,15, 1, 0, 0, 0, 4,15,15, 4, 0, 0)), 0);
		self.assertEqual(c.classify(( 0, 3,12,16,16,16, 4, 0, 0, 8,11, 6, 4,12,15, 0, 0, 1, 0, 0, 6,15,10, 0, 0, 0, 0, 7,16, 7, 0, 0, 0, 0, 0,10,14, 1, 0, 0, 0, 0, 0, 1,15, 9, 0, 0, 0, 0, 6, 2,13,12, 0, 0, 0, 2,16,16,14, 3, 0, 0)), 3);
		self.assertEqual(c.classify(( 0, 1, 8,16,14, 0, 0, 0, 0, 4,15, 9,16, 3, 0, 0, 0, 1, 4, 7,16, 0, 0, 0, 0, 0, 0,11,16, 9, 0, 0, 0, 0, 0, 0, 5,15, 5, 0, 0, 0, 0, 0, 0,15, 5, 0, 0, 0,15, 9, 9,15, 2, 0, 0, 0, 6,13,10, 4, 0, 0)), 3);
		self.assertEqual(c.classify(( 0, 0, 1,13,10, 0, 0, 0, 0, 0,10,16, 7, 0, 0, 0, 0, 3,16, 7, 0, 0, 0, 0, 0, 3,16, 3, 0, 0, 0, 0, 0, 8,16, 6, 8, 7, 0, 0, 0, 3,15,16,16,16, 8, 0, 0, 0, 9,16,16,16, 5, 0, 0, 0, 0, 8,15, 9, 0, 0)), 6);
		self.assertEqual(c.classify(( 0, 0, 2,13,10, 4, 0, 0, 0, 0, 0,16,16,11, 0, 0, 0, 0, 0,13,16,15, 0, 0, 0, 0, 1,14,16,11, 0, 0, 0, 0, 4,16,16, 6, 0, 0, 0, 0, 3,16,14, 2, 0, 0, 0, 0, 7,16,16, 3, 0, 0, 0, 0, 4,13,16, 4, 0, 0)), 1);
		self.assertEqual(c.classify(( 0, 0, 4,15,16, 7, 0, 0, 0, 0,13,12,16, 9, 0, 0, 0, 0, 2, 1,16, 7, 0, 0, 0, 0, 0, 5,15, 3, 0, 0, 0, 0, 0,14,10, 0, 0, 0, 0, 0, 6,16, 2, 0, 0, 0, 0, 0, 9,16,11, 7, 0, 0, 0, 0, 5,16,16,10, 0, 0)), 2);
		self.assertEqual(c.classify(( 0, 0, 7,16,11, 0, 0, 0, 0, 5,15,12,16, 3, 0, 0, 0, 6,16,14,16, 7, 0, 0, 0, 1, 8,12,16, 8, 0, 0, 0, 0, 0, 0, 6,15, 2, 0, 0, 0, 0, 0, 0,16, 7, 0, 0, 0, 0, 0, 2,13, 8, 0, 0, 0, 8,16,16,14, 4, 0)), 9);
		self.assertEqual(c.classify(( 0, 0, 1,13,14,11, 0, 0, 0, 0,10,12,12,16, 4, 0, 0, 0,15, 0, 2, 9, 6, 0, 0, 5,13, 0, 0, 6, 9, 0, 0, 5,12, 0, 0, 5, 7, 0, 0, 1,13, 2, 0, 9, 4, 0, 0, 0,12,11, 7,11, 0, 0, 0, 0, 2,15,12, 3, 0, 0)), 0);
		self.assertEqual(c.classify(( 0, 0, 9,16,10, 1, 0, 0, 0, 9,16, 9,16, 6, 0, 0, 0,16, 9, 3,16, 5, 0, 0, 0, 3, 6,12,16,10, 0, 0, 0, 0, 1,10, 9,15, 8, 0, 0, 0, 0, 0, 0, 9,15, 0, 0, 0, 3, 9, 2,13,12, 0, 0, 0, 7,16,16,15, 4, 0)), 3);
		self.assertEqual(c.classify(( 0, 1,12,13, 9, 5, 0, 0, 0, 5,16,11,15,16, 0, 0, 0, 4,16, 5, 8,16, 4, 0, 0, 2,13,16,16,16, 5, 0, 0, 0, 0, 3, 4,15, 6, 0, 0, 0, 0, 0, 1,15, 6, 0, 0, 0,11, 9,12,16, 2, 0, 0, 0,11,16,14, 8, 0, 0)), 9);
		self.assertEqual(c.classify(( 0, 0, 0, 8,14, 5, 0, 0, 0, 0, 0, 9,16,14, 2, 0, 0, 0, 0,11,16,13, 1, 0, 0, 0, 6,16,16, 7, 0, 0, 0, 3,13,16,16, 4, 0, 0, 0, 3,11,15,16,12, 0, 0, 0, 0, 0,10,16,15, 3, 0, 0, 0, 0, 8,16,15, 6, 0)), 1);
		self.assertEqual(c.classify(( 0, 0, 4,12, 0, 0, 0, 0, 0, 0,14, 6, 0, 0, 0, 0, 0, 4,16, 4, 0, 0, 0, 0, 0, 7,16, 1, 0, 0, 0, 0, 0, 8,16,16,16,13, 1, 0, 0, 5,16, 7, 9,16, 5, 0, 0, 1,14,12, 4,16, 5, 0, 0, 0, 3,15,16, 8, 0, 0)), 6);
		self.assertEqual(c.classify(( 0, 0, 1, 7,16,12, 0, 0, 0, 0, 3,15,16,12, 0, 0, 0, 5,13,16,16, 9, 0, 0, 0, 5,14,16,16, 8, 0, 0, 0, 0, 4,16,16, 7, 0, 0, 0, 0, 0,11,16,12, 0, 0, 0, 0, 0, 8,16,16, 5, 0, 0, 0, 0, 6,14,13, 5, 0)), 1);
		self.assertEqual(c.classify(( 0, 0,13,10, 2, 8, 0, 0, 0, 2,16,13,13,14, 0, 0, 0, 0,14, 4,12,11, 0, 0, 0, 0,12,13,16, 5, 0, 0, 0, 0, 3,16,13, 0, 0, 0, 0, 0, 9,16, 9, 0, 0, 0, 0, 0,16,16,10, 0, 0, 0, 0, 0,11,13, 2, 0, 0, 0)), 8);



def main():
    unittest.main()

if __name__ == '__main__':
    main()