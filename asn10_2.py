name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour = dict()
lst = list()

for line in handle:
	#if not line.startswith('From:') : continue	
	if line.startswith('From '):
		words = line.split()
		time = words[5].split(':')
		if time[0] not in hour:
			hour[time[0]] = 1
		else:
			hour[time[0]] +=1
for key, val in list(hour.items()):
	lst.append((key,val))
	lst.sort()

for key,val in lst:
	print key,val			