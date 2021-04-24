nested1 = [['a','b','c'], ['d','e'], ['f','g','h']]

print('Example 1 ********')
for x in nested1:
	print('Level 1:')
	for y in x:
		print('     Level 2: ' + y)

