correct = 'a123456'
i = 3
while i > 0:
    pw = input('請輸入密碼： ')
    if pw == correct:
        print('登入成功')
        break
    else:
        i -= 1
        print('密碼錯誤！還有',i,' 次機會')