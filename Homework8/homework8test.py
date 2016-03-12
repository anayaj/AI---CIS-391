import unittest
from homework8 import *
import os
from os import listdir

class MyTests(unittest.TestCase):

	def test1(self):
		c = load_corpus("brown_corpus.txt")
		self.assertEqual(c[1402], [('It', 'PRON'), ('made', 'VERB'), ('him', 'PRON'), ('human', 'NOUN'), ('.', '.')])

	def test2(self):
		c = load_corpus("brown_corpus.txt")
		t = Tagger(c)
		self.assertEqual(t.most_probable_tags(["The", "man", "walks", "."]), ['DET', 'NOUN', 'VERB', '.'])
		self.assertEqual(t.most_probable_tags(["The", "blue", "bird", "sings"]), ['DET', 'ADJ', 'NOUN', 'VERB'])

	def test3(self):
		c = load_corpus("brown_corpus.txt")
		t = Tagger(c)
		s = "I am waiting to reply".split()
		self.assertEqual(t.most_probable_tags(s), ['PRON', 'VERB', 'VERB', 'PRT', 'NOUN'])
		self.assertEqual(t.viterbi_tags(s), ['PRON', 'VERB', 'VERB', 'PRT', 'VERB'])
		s = "I saw the play".split()
		self.assertEqual(t.most_probable_tags(s), ['PRON', 'VERB', 'DET', 'VERB'])
		self.assertEqual(t.viterbi_tags(s), ['PRON', 'VERB', 'DET', 'NOUN'])

def main():
    unittest.main()

if __name__ == '__main__':
    main()