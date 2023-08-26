member = [111, 222, 333, 444, 555]
print(member)

member.remove(111)
print(member)

member.insert(1, 999)
print(member)
member.append(123)
print(member)
member.extend([666, 777])
print(member)
member[0] = "aaa"
print(member)
r = member.pop(1)
print(r)
print(member)

list2 = member
list2[0] = 111222
print(member)

size = int(len(member))
list3 = member[0 : size]
list3[0] = 111555
print(list3)
print(member)

list4 = member[:]
list4[0] = 1115553
print(list4)


list5 = list3 + list4
print(list5)

list6 = list5 * 2
print(list6)

print(111555 in list6)

print(list6.count(777))
print(list6.index(777))

list6.reverse()
print(list6)

list6.sort()
print(list6)

list6.sort(reverse = True)
print(list6)

newlist = []
for each in list6:
	if each not in newlist:
		newlist.append(each)

print("newlist = " + str(newlist))

del member[0]
print(member)
del member
#print(member)