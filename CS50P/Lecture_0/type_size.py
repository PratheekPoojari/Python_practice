import sys

a = 1
b = 2.34
c = 22 / 7
d = 123 // 12 # Rounds the resulting division value to the number closest to negative infinity.
name = "Pratheek"

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(name), name)

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(name))
