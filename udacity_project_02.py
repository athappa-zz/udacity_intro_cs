#exercise 5

import csv

'''
with open('turnstile_110507.txt', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print row

row1 = ['a', 'b', 'c']
row2 = ['d', 'e', 'f']
data = []
data.append(row1)
data.append(row2)

with open('test_format.txt', 'wb') as g:
	writer = csv.writer(g)
	writer.writerows(data)
'''

for name in filenames:
	with open(name, 'rb') as f:
	rdr = csv.reader(f)
	with open("updated_" + name, 'wb') as g:
		wr = csv.writer(g)
		for row in rdr:
			head = row[:2]
			tail = row[3:]
			recordsCnt = len(tail)/5
			for rIndex in xrange(recordsCnt):
				newRow = head + tail[5*rIndex : 5*rIndex + 5]
				wr.writerow(newRow)