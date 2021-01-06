password = 'a123456'
x = 5
while x > 0:
	x -= 1
	pwd = input('請輸入你的密碼: ')
	if pwd == password :
		print('登入成功!')
		break
	else :
		print('密碼錯誤!')
		if x > 0:
			print('還有', x, '次機會')
		
		if x == 1:
			print('最後一次機會喔')
if x == 0:		
	print('偷帳的?')