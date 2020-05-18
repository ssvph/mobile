import csv


with open('data.csv') as data:
	readData = csv.reader(data, delimiter=',')

	phoneNumber = '915783624'
# rate of calls by tariff
	kOut = 2
	kIn = 0
	kSms = 1

	for row in readData:
		if phoneNumber in row[1]:
			outCall = float(row[3])
			nSms = float(row[4])
		if phoneNumber in row[2]:
			inCall = float(row[3])

	resOutCall = outCall * kOut
	resInCall = inCall * kIn
	if nSms >= 10:
		resSms = (nSms - 10) * kSms
	else:
		nSms = 0

#		print 'Output Calls =', resOutCall
#		print 'Input Calls =', resInCall
#		print 'Number Sms =', resSms

data.close()
sum = resOutCall + resInCall + resSms
#print('Cash =', sum)



