dict1 = {1:"one", 2:"two", 3:"Three"}
print(dict1)
print(dict1[1])

dict2 = dict(x="one", y="two", z="Three")
print(dict2['y'])

dict2['y'] = "xxxxxx"
print(dict2)

dict2['m'] = "xxasdfasdfas"
print(dict2)


print('m' in dict2)
print(dict2.keys())
print(dict2.values())
print(dict2.items())

dict2.clear()
print(dict2)

dict2['m'] = "xxasdfasdfas"
print(dict2)

dict2.setdefault(4, "four")
print(dict2)