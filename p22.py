g = lambda x: x*x
print(g(5))

g = lambda x,y : x+y
print(g(7,8))


def func(x):
	return lambda y : x*y

y = func(6)
print(y(5))