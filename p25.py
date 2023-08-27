def fab(n):
	a1 = 1
	a2 = 1
	a3 = 1

	if (n < 1):
		print("input error!")
		return -1

	while (n -2) > 0:
		a3 = a1 + a2
		a1 = a2
		a2 = a3
		n -= 1

	return a3



def fab_rs(n):
	if (n < 1):
		print("input error!")
		return -1
	if n == 1 or n == 2:
		return 1

	return fab_rs(n-1) + fab_rs(n-2)


def hannota(n, x, y, z):
	if n == 1:
		print(x, "-->", z)
	else:
		hannota(n-1, x, z, y)
		print(x, "-->", z)
		hannota(n-1, y, x, z)



value = fab(15)
print(value)

value = fab_rs(15)
print(value)


hannota(3, "x", "y", "z")