num = [1, 3, 5]
double = [x * 2 for x in num]

print(double)


# example 2 - text
friends = ['Amo', 'Ben', 'Adrian', 'Charles', 'Ali', 'Danny']

start_with_a = []

for name in friends:
	if name.startswith('A'):
		start_with_a.append(name)

print(start_with_a)

friends = ['Amo', 'Ben', 'Adrian', 'Charles', 'Ali', 'Danny']

start_with_a = [f for f in friends if f.startswith('A')]

print(start_with_a)