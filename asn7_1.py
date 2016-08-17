# Use words.txt as the file name
filename = raw_input("Enter file name: ")
filehandle = open(filename)
for line in filehandle:
	line = line.upper().strip()
	print line