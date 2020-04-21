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
	arrayTime = []
	arrayByte = []

# tariffing
	for row in readData:
		if len(row) == 48:
			if row[3] == '217.15.20.194':
				countByte += int(row[12])
				arrayByte.append(int(row[12]))
				arrayTime.append(row[0])
			if row[4] == '217.15.20.194':
				arrayByte.append(int(row[12]))
				arrayTime.append(row[0])
				countByte += int(row[12])

# output the result
	MB = countByte / 1000000
	resultSum = MB * k
	print('Sum =', '%.2f' % resultSum)

	arrayTime.pop(0)
	arrayByte.pop(0)

# plotting averages graph
	b3_0 = 0
	b3_3 = 0
	b4_0 = 0
	b4_3 = 0
	for i in range(len(arrayTime)):
		if '25 03:0' in arrayTime[i]:
			b3_0 += int(arrayByte[i])
		if '25 03:1' in arrayTime[i]:
                        b3_0 += int(arrayByte[i])
		if '25 03:2' in arrayTime[i]:
                        b3_0 += int(arrayByte[i])
		if '25 03:3' in arrayTime[i]:
                        b3_3 += int(arrayByte[i])
		if '25 03:4' in arrayTime[i]:
                        b3_3 += int(arrayByte[i])
		if '25 03:5' in arrayTime[i]:
			b3_3 += int(arrayByte[i])
		if '25 04:0' in arrayTime[i]:
                        b4_0 += int(arrayByte[i])
		if '25 04:1' in arrayTime[i]:
                        b4_0 += int(arrayByte[i])
		if '25 04:2' in arrayTime[i]:
			b4_0 += int(arrayByte[i])
		if '25 04:3' in arrayTime[i]:
                        b4_3 += int(arrayByte[i])
		if '25 04:4' in arrayTime[i]:
                        b4_3 += int(arrayByte[i])
		if '25 04:5' in arrayTime[i]:
                        b4_3 += int(arrayByte[i])

# average value of In Byte and Date First Seen
	arrByte = [int(b3_0/1079), int(b3_3/1079), int(b4_0/1079), int(b4_3/1079)]
	arrTime = ['03:00 - 03:29', '03:30 - 03:59', '04:00 - 04:29', '04:30 - 04:59']

	plt.plot(arrTime, arrByte)
	plt.title('Graph In Byte of Date First Seen')
	plt.xlabel('Time First Seen')
	plt.ylabel('In Byte')
	plt.show()
