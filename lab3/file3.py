import file1
import file2
import pdfkit

min3 = file1.outCall + file1.nSms
summa = file1.sum + file2.resultSum
print("CDR ", min3,"minutes")
print("NetFlow", '%.2f' % file2.MB,"Mb\n")
print("Итого к оплате:", '%.2f' % summa)
print("В том числе НДС:", '%.2f' % (summa * 0.2))
print("Всего к оплате:", '%.2f' % (summa * 1.2))

options = {
	'no-background': None,
}
pdfkit.from_file('lab3.html', 'result_file.pdf', options=options)
