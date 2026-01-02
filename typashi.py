for i in range(5):
    num = int(input('enter num : '))
    if num % 15 == 0:
        print('dividible by 15')
    elif num % 5 == 0:
        print('divisible by 5')
    elif num % 3 == 0:
        print('divisible by 3')
    else:
        print('not divisible by 15,5,3')
    if num % 2 == 0:
        print('its even')
    else:
        print('its odd')
print('\n\n')

for i in range(6):
    for j in range(1, i+1):
        print(j, end='')
    print()
print('\n\n')

for i in range(5, -1, -1):
    for j in range(i-1, -1, -1):
        print('*', end=' ')
    print()

for i in range(6):
    for j in range(1, i+1):
        print(i*j, end=' ')
    print()

for i in range(6):
    for s in range(6-i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for x in range(i-1, 0, -1):
        print(x, end=' ')
    print()
