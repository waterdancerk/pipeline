import os
from os import walk
from os.path import exists
from Bio import SeqIO
file_list = []
for (dirpath, dirnames, filenames) in walk("/Users/kate/python"):
	file_list.extend(filenames)
print(file_list)
count = 0
for filen in file_list:
	if filen[0:1]!=".":
		handle = open("/Users/kate/python/"+filen, "rU")
		for (record) in SeqIO.parse(handle, "fasta"):
			count += 1
		handle.close()
print (count)
