def polindrom():
	s= input('Введите слово: ')
	len_str = len(s)
	l = len_str//2

	for i in range(l):
		if s[i] == s[-1-i]:
			polindrom = True
		else:
			polindrom = False

	if 	polindrom == True:
		print('Слово является полиндромом')
	else:
		print('Слово не является полиндромом')

polindrom()
