strValue = "hello my world !!!"
str1list = strValue.split(' ')
print(str1list)

str2 = '#'.join(str1list)
print(str2)

str3 = strValue.replace(' ', '-')
print(str3)


strformat = "{0} love {1} {{aaaa}}"
str4 = strformat.format("I", "yuyyu")
print(str4)

print('%d 的16进制是 %x' % (16, 16))