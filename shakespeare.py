import sys
import string
def words_with_counts(script, theword):
	file_object = open(script, "r")
	file_read = file_object.read()
	remove = "\n"
	read2 = file_read.replace('\n'," ")
	lis = read2.split (" ")
	lis = [''.join(c for c in s if c not in string.punctuation) for s in lis]
	lis = [s for s in lis if s]
	dic = {}
	for raw_word in lis:
		word = raw_word.lower()
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	try:
		print(dic[theword])
	except KeyError:
		print ("Word is not in file.")
x = sys.argv[1:]
a = x[0]
b = x[1]
words_with_counts(a, b)

