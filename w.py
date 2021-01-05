password = 'a123'
x = 2
while True:
	password = input('please enter your password: ')
	if password == 'a123':
		print('成功登入!')
		break
	elif x <= 0:
		print('over')
		break
	elif password != 'a123' and x >= 2:
		print('密碼錯誤, 還有2次機會')
		x = x - 1
	elif password != 'a123' and x >= 1:
		print('密碼錯誤, 還有1次機會')
		x = x - 1 