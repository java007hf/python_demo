
import random
member = ["aaa", "bbb", "cccc"]

for strValue in member:
	print(strValue)


for i in range(2, 15, 2):
	print(i)

for char in list("abadsfasdfasd"):
	print(char)


empty = []
for randomNum in range(10):
	empty.append(random.randint(1, 10))


print(empty)
print(len(empty))

empty.extend(["aaa", "aaa"])
print(empty)


empty.insert(0, 89898)
print(empty)


temp = empty[0]
empty[0] = empty[1]
empty[1] = temp
print(empty)

empty.remove("aaa")
print(empty)

currentStr = "aaa"
temp = input("please enter a str\n")

while True:
	if (temp == currentStr):
 		break;

	temp = input("not right, please input again\n")

print("you are right")


