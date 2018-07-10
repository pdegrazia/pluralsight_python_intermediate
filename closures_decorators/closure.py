def outer():
	x = 'inner'

	def inner():
		print(x)

	return inner


f = outer()

f()

f = outer

print(f())

g = f()
g()

print(g.__closure__)
