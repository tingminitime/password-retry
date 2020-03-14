# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出"登入成功!"
# 如果不正確就印出"密碼錯誤! 還有_次機會!"

#第一次自己打
chance = 3
while chance > 0:
	password_input = input('請輸入密碼: ')
	password = 'a123456'
	chance = chance - 1
	if password_input == password:
		print('登入成功!')
		break
	elif chance > 0:
		print('密碼錯誤! 還有', chance, '次機會')
	else:
		print('登入失敗')

# 解答
# password = 'a123456'
# i = 3 # 剩餘機會
# while True:
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功!')
# 		break # 逃出迴圈
# 	else:
# 		i = i - 1
# 		print('密碼錯誤! 還有', i, '次機會')
# 		if i == 0:
# 			print('登入失敗')
# 			break