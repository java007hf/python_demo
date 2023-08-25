import random

print("hello")

isFinish = False
currentValue = random.randint(1, 10)
print("currentValue " + str(currentValue))

a = "520"
b = int(a)
print(b)


a = "521.4"
b = float(a)
print(b)


print(10/4)
print(10//4)
print(10%4)
print(4**3)

if currentValue > 5:
	print(">5")
elif currentValue < 3:
	print("<3")
else:
	print("else")


times = 3
while isFinish != True and times > 0:
	temp = input("input a number")

	typevale = type(temp)
	print(typevale)

	print(isinstance(temp, str))

	value = int(temp)
	times -= 1
	if value == currentValue:
		isFinish = True
	else :
		isFinish = False

print("game finish")