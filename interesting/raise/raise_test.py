def foo():
	print('hello')
	try:
		print(a)
	except NameError:
		print('in except block')
#		raise
	print('after raise')

foo()
