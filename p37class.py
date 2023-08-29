class A:
	str1 = "123"
	int1 = 111

	def func1(self):
		print(self.str1)

	def func2(self):
		print(str(self.int1))



a = A()
a.func1()

a.str1 = "123123"
a.func1()