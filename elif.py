# else if
age = input('Enter your age: ')
age = int(age)
if age < 13:
	print('Elementary School')
elif age >= 13 and age < 18 :
	print('Junior High School & Senior High School')
elif age >= 18 and age <22 :
	print('University')
else:
	print('Society')	