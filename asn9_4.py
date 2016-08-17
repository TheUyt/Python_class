name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()
largest = None
eadd = None
for line in handle:
	if not line.startswith('From:') : continue
	
	if line.startswith('From'):
		words = line.split()
		email = words[1]
		#print email
		if email not in sender:
			sender[email] = 1
		else:
			sender[email] += 1
for (sender,values) in sender.items():
	if largest is None or values > largest:
		largest = values
		eadd = sender
		#print sender, largest
print eadd, largest
#print sender.keys()
#print sender.values()
#print sender.items()
#print sender.get(email,0)