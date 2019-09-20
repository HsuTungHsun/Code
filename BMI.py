weight = input('Enter your weight/kg: ')
height = input('Enter your height/m: ')
weight = float(weight)
height = float(height)
#height = height / 100
bmi = weight / height / height
#bmi = str(bmi)
#	print('bmi')


if bmi < 18.5 :
	print('Too thin')
elif bmi > 18.5 and bmi < 24 :
	print('Normal')
elif bmi > 24 and bmi < 27 :
	print('Overweight')
elif bmi > 27 and bmi < 30 :
	print('A little fat')
elif bmi > 30 and bmi < 35 :
	print('Too Fat')
elif bmi >= 35 :
	print('Super Fat')
else :
	print('U are stupid')