correct = 'a123456'
i = 3
while i > 0:
    i -= 1
    pw = input('請輸入密碼： ')
    if pw == correct:
        print('登入成功')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('沒機會嘗試！要鎖帳號了！')