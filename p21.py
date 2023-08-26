
x = 10
def log(func):
	x = 5
	def wrapper(*p):
		nonlocal x
		x = x + 1
		print("======" + str(x))
		func(*p)
		print("======")
	return wrapper

def eventTrack(func):
	def wrapper(*p):
		print(*p)
		print("xxxxxxx")
		func(*p)
		print("yyyyyy")
	return wrapper

@eventTrack
@log
def eat(*p) :
	print("eat %s===%s"% (p[0], p[1]))


def wrapper(func):
	print("======")
	func()
	print("======")

eat('cccc', 'zzzz')

#eat = log(eat)
#eat()

#wrapper(eat)