password = 'a123'
x = 3 # 輸入機會次數
while True:
	pwd = input('please enter your password: ')
	if pwd == password:
		print('成功登入!')
		break
	else:
		x = x - 1
		print('密碼錯誤, 還有', x, '次機會')
		if x == 0:
			break