username = input('enter username : ')
password = input('enter password : ')
is_admin = True

if is_admin:
    print('welcom,admin!')
elif username == 'nooha' and password == 'star123':
    print('WElcome,Nooha!')
else:
    print('access denied')
