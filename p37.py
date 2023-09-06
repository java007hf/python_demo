from p37class import A
from p37classb import B
from p37classb import static_func
from p37classc import C

a = A(55)
a.func1()
a.func2()

a.setValue(999)
print(a.getValue())


b = B(99)
b.func1()
b.func2()

print(issubclass(A, B))
print(issubclass(B, A))
print(hasattr(b, "int1"))
print(setattr(b, "int1", 8888))
print(getattr(b, "int1"))
static_func()

C.static_func()
