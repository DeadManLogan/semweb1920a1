import re
import csv

rexp = re.compile("[:/\\?#\\[\\]@!\\$&'\\(\\)\\*\\+,;=< >\" \\{\\}\\|\\\\^`]")

def q_f(m):
    return '%{:02X}'.format(ord(m.group(0)))

def uri_quote(s):
    return rexp.sub(q_f,s)



with open('out02.csv', 'r', newline = '',encoding = 'utf-8') as ifp, open('out03.csv', 'w', newline = '', encoding = 'utf-8')as ofp:

	ir = csv.reader(ifp)
	ow = csv.writer(ofp)

	for i in ir:
		a = i[0]
		b = ('http://host/p16grig/vocabulary#' + i[1])
		c = i[2]

		if i[1] != 'Ωρα%20Απο' and i[1] != 'Ωρα%20Εως' and i[1] != 'Ημέρα':
			c = ('http://host/p16grig/resource/' + i[2])

		ow.writerow([a, b, c])