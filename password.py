password = 'a123456'
i = 3
while i > 0 :
	i = i - 1
	pwd = input('Enter your password: ')
	if pwd == password:
		print('Success')
		break
	else:
		print('Error')	
		if i > 0:
			print('You still have', i ,'Times chance')
		else:
			print('You are not the user')
		