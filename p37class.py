class A:
	str1 = "123"
	int1 = 111
	__privateValue = 123444

	def __init__(self):
		self.str1 = "hello init"
		

	def __init__(self, v):
		self.int1 = 989898
		self.abc = "dd"

	def func1(self):
		print(self.str1)
		print(self.abc)

	def func2(self):
		print(str(self.int1))

	def setValue(self, v):
		self.__privateValue = v

	def getValue(self):
		return self.__privateValue
