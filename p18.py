def myFunc():
	print('func')

def sumValue(a, b):
	return a+b

def changeValue(b):
	b = 10

def defaultArgc(name="123", words="bbbb"):
	print(name + "->" + words)

def test(*params):
	print(len(params))
	print(params[0])

def test1(params):
	print(len(params))
	print(params[0])

for i in range(10):
	myFunc()

print(sumValue(1, 2))

b = 4
changeValue(b)
print(b)
defaultArgc()
defaultArgc(words="acaca")
defaultArgc(name="1111")

list1 = [11,22,33,4,5,23]
test(list1)
test(11,22,33,4,5,23)

test1(list1)
