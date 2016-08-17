name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()

for line in handle:
	if not line.startswith('From:') : continue
	
	if line.startswith('From'):
		words = line.split()
		email = words[1]
		print email
		#if email not in sender:
		#	sender[email] = 1
		#else:
		#	sender[email] += 1