def bnp(number):
	if number < -10:
		return -int(''.join(sorted(str(number)[1:])))
	elif number < 10:
		return number
	else:
		return int(''.join(sorted(str(number), reverse=True)))


list = [0, 5, 13, 3328, -32, -5]
for i in list:
	print bnp(i)
