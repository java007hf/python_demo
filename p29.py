def readfile(f):
 	print(f.read())

f = open(r"D:\workspace\python_demo\record.txt")
readfile(f)

a_record = []
b_record = []

f.seek(0, 0)
for each in f:
	(role, spoken) = each.split(":", 1)
	print(role)
	print(spoken)

	if (role == 'a'):
		a_record.append(spoken)
	elif (role == 'b'):
		b_record.append(spoken)

print(a_record)
print(b_record)


a_filepath = r"D:\workspace\python_demo\a.txt"
b_filepath = r"D:\workspace\python_demo\b.txt"

a_file = open(a_filepath, "w")
b_file = open(b_filepath, "w")

a_file.writelines(a_record)
b_file.writelines(b_record)

a_file.close()
b_file.close()