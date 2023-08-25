count = 5
count1 = 5

def myFunc():
	global count1
	count = 10
	count1 = 11

myFunc()
print(count)
print(count1)