import re
import csv
import datetime

rexp = re.compile("[:/\\?#\\[\\]@!\\$&'\\(\\)\\*\\+,;=< >\" \\{\\}\\|\\\\^`]  ")

def q_f(m):
    return '%{:02X}'.format(ord(m.group(0)))

def uri_quote(s):
    return rexp.sub(q_f,s)



with open('text_out03.csv', 'r', newline = '',encoding = 'utf-8') as ifp, open('text_out04.csv', 'w', newline = '', encoding = 'utf-8')as ofp:

	ir = csv.reader(ifp)
	ow = csv.writer(ofp)

	'''t = datetime.time(00)
	print(t.hour, t.minute, t.second)'''

	for i in ir:
		a = ('_:' + i[0])
		b = ('<' + i[1] + '>')
		c = i[2]	

		if i[1] == 'http://host/p16grig/vocabulary#Ωρα%20Απο' or i[1] == 'http://host/p16grig/vocabulary#Ωρα%20Εως':
			c = ('"' + i[2] + ':00"' )

		if i[1] == 'http://host/p16grig/vocabulary#Ημέρα':

			c = ('"' + i[2] + '"' )

		ow.writerow([a, b, c])