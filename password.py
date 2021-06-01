pwd = 'a123456'
i = 3
while i > 0:
    i -= 1
    guess = input('Enter password: ')
    if guess == pwd:
        print('log in successfully')
        break
    else:
        if len(guess) > 7: 
            print('excess maximum password length(7 digi)')
            if i > 0:
                print(i, 'time(s) remains')
        elif guess != pwd:
            print('password incorrect')
            if i > 0:
                print(i, 'time(s) remains')