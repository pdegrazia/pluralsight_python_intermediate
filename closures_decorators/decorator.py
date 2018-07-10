#very similar to closure, but used to "decorate" functions


def my_decorator(f):
	def inner():
		print('about to call function')
		return f
	return inner


@my_decorator
def test_function():
	print('inside test function')


test_function()


def escape_unicode(f):
	def wrap(*args, **kwargs):
		x = f(*args, **kwargs)
		return ascii(x)
	return wrap


@escape_unicode
def unicode_string():
	return 'Sarà un vertice a tre'


print(unicode_string())