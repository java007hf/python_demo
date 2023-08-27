import os

print(os.getcwd())
print(os.listdir())

file = open("sss.txt", "w")
os.mkdir("test")
os.makedirs(r".\a\b\cragadga")

file.close()

print(os.path.abspath("sss.txt"))

print(os.path.split(r"c:\sss.txt"))
print(os.path.splitext(r"c:\sss.txt"))
print(os.path.getsize(r"D:\workspace\python_demo\demo.py"))

os.rename("sss.txt", "bbb.txt")

os.remove(os.path.abspath("bbb.txt"))
os.rmdir("test")
os.removedirs(r".\a\b\cragadga")

#os.system("calc")

#for i in os.walk(r      "c:\\"):
#	print(i)