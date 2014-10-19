import unittest
from descriptivestats import DescriptiveStats
from inputtypeerror import InputTypeError

class DSTest(unittest.TestCase):

	def test_for_not_A(self):
		self.assertRaises(InputTypeError, DescriptiveStats, "/Users/kate/python/top.fasta", "b")

	def test_for_not_Q(self):
		self.assertRaises(InputTypeError, DescriptiveStats, "/Users/kate/python/top.fasta", "b")

	def test_for_invalid_path(self):
		self.assertRaises(InputTypeError, DescriptiveStats, "/Users/kate/python/test.fasta", "a")

	def test_for_valid_path_to_not_text(self):
		self.assertRaises(UnicodeDecodeError, DescriptiveStats, "/Users/kate/python/__pycache__/inputtypeerror.cpython-34.pyc", "a")

	def test_for_valid_path_to_not_fasta(self):
		ds=DescriptiveStats("/Users/kate/python/testdata.txt", "A")
		self.assertEqual(ds.read_count(),0)

	def test_for_read_total(self):
		ds=DescriptiveStats("/Users/kate/python/top.fasta", "A")
		self.assertEqual(ds.read_count(),4)

	def test_for_frequency_by_length(self):
		ds=DescriptiveStats("/Users/kate/python/top.fasta", "A")
		#the frequency of the lenghts of sequences in the top.fasta test file
		actual_freq_by_length = {9:1,10:1,11:2}
		self.assertEqual(actual_freq_by_length,ds.frequency_by_length())

	def test_for_frequency_by_identity(self):
		#the frequency of distict sequences in the top.fasta test file
		ds=DescriptiveStats("/Users/kate/python/top.fasta", "A")
		actual_frequency_by_identity={"ACTGGACCT":1,"ACTGGACCTA":1,"ACTGGACCTAA":2}
		self.assertEqual(actual_frequency_by_identity,ds.frequency_by_identity())


if __name__ == "__main__":
	unittest.main();





