password = 'a123'
x = 3 # 輸入機會次數
while x > 0:
	x = x - 1
	pwd = input('please enter your password: ')
	if pwd == password:
		print('成功登入!')
		break
	else:
		print('密碼錯誤')
		if x > 0:
			print('還有' , x, '次機會')
		else:
			print('冇機會啦! 鎖帳了')