from p37class import A
class B(A):
	def __init__(self, v):
		A.__init__(self, v)
		self.h = True
		self.int1 = 888

def static_func():
	print("static func")