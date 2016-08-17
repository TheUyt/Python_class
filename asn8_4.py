fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
final = list()
for line in fh:
	lst = line.split()
	#print ('list length:'),len(lst)
	#print lst
	for words in lst:
		if words not in final:
			#print words
			final.append(words)
final.sort()
print final