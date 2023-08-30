class A(str):
	def __new__(cls, string):
		stringValue = string.upper()
		print(cls)
		return str.__new__(cls, stringValue)

	def __init__(self, string):
		print("init ===" + str(self) + "  " + string)

	def __del__(self):
		print("del ====")