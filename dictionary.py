friends_age = {"Anna":15, "Qing":13, "Bob":15}

print(friends_age)
print(friends_age["Qing"])


# Example 2
print("\nExample - 2")
friends = [
	{"name": "Qing", "Age": 13},
	{"name": "Anna", "Age": 15},
	{"name": "Bob", "Age": 14},
	{"name": "Thomas", "Age": 16},
]

print(friends[2]["name"])

# Example 3

student_attendence = {"Adam": 70, "Ben": 80, "Charles":100}

print("\nExample - 3")
for student in student_attendence:
	print(student)
	print(f"{student},{student_attendence[student]}")

# Example 4

student_attendence = {"Adam": 70, "Ben": 80, "Charles":100}

print("\nExample - 4")
for student, attendence in student_attendence.items():
	print(f"{student},{attendence}")


# Example 5

student_attendence = {"Adam": 70, "Ben": 80, "Charles":100}

print("\nExample - 5")
attendence_values = student_attendence.values() 
print(sum(attendence_values)/len(attendence_values))

# Example 6
print("\nExample 6")
d = {'key1': {'a':5, 'c':90, 5:50}, 'key2': {'b':3, 'c':"yes"}}
print(d)
d[5] = {1:2, 3:4}
print(d)
d['key1']['d']=d['key2']
print(d)