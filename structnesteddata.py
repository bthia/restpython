nested = [1, 2, ['a','b','c'],['d','e'],['f','g','h']]

for x in nested:
	print("Level 1: ")
	if type(x) is list:
		for y in x:
			print("   Level 2: {}".format(y))
	else:
		print(x)

