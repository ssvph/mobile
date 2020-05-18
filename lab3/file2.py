import csv
import matplotlib.pyplot as plt

with open('data2.csv') as data:
	readData = csv.reader(data, delimiter=',')

# row[12] - In Byte
# row[3] - Src IP Addr
# row[4] - Dst IP Addr
# row[0] - Date First Seen

	countByte = 0
	k = 0.5

# tariffing
	for row in readData:
		if len(row) == 48:
			if row[3] == '217.15.20.194':
				countByte += int(row[12])
			if row[4] == '217.15.20.194':
				countByte += int(row[12])

# output the result
	MB = countByte / 1000000
	resultSum = MB * k
#	print('Sum =', '%.2f' % resultSum)

