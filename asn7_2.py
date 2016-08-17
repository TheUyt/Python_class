# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
floatmath = 0
for line in fh:
	if line.startswith("X-DSPAM-Confidence:"):
		count = count + 1
		#print count
		pos = line.find(':')
		number = line[pos+1:]
		result = float(number)
		floatmath = floatmath + result
		#print floatmath
	if not line.startswith("X-DSPAM-Confidence:") : continue
ave = floatsum/count
print ("Average spam confidence:"), ave