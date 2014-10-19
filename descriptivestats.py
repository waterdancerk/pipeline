from Bio import SeqIO
import sys
import os
from os import walk
from os.path import exists
from inputtypeerror import InputTypeError
from collections import defaultdict


class DescriptiveStats(object):
	

	def __init__(self,fpath,ftype):
		self.read_counter=0
		self.length_frequency_dict=defaultdict(int)
		self.identity_frequency_dict=defaultdict(int)
		#test path valid
		if os.path.exists(fpath):
			self.fpath=fpath
		else:
			raise InputTypeError("You must specify a valid file path")

		#test file type valid
		if (ftype=="A" or ftype=="a"):
			self.ftype="fasta"
		elif(ftype=="Q" or ftype=="q"):
			self.ftype="fastq"
		else:
			raise InputTypeError("You must specify A/a or Q/q")
		self.run_all()

	def run_all(self):
		handle = open(self.fpath, "rU")
		for (record) in SeqIO.parse(handle, self.ftype):
			self.__private_add_to_count()
			self.__private_frequency_by_length(record)
			self.__private_frequency_by_identity(record)
		handle.close();

	def __private_add_to_count(self):
		self.read_counter+=1
		
	def read_count(self):
		return self.read_counter

	def __private_frequency_by_length(self, record):
		self.length_frequency_dict[len(record.seq)] += 1

	def frequency_by_length(self):
		return self.length_frequency_dict

	def __private_frequency_by_identity(self,record):
		self.identity_frequency_dict[str(record.seq)] += 1

	def frequency_by_identity(self):
		return self.identity_frequency_dict


		

		





