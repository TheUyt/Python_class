fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
words = list()
fh = open(fname)
count = 0
linenum = 0

for line in fh:
	#linenum = linenum + 1
	if not line.startswith('From:') : continue
	if line.startswith('From'):
		count = count + 1
		#print linenum, count
		words = line.split()
		print words[1]

print "There were", count, "lines in the file with From as the first word"