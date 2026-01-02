frnds = []
for i in range(3):
    frnds.append(input('enter name:'))
print(frnds)
for frnd in frnds:
    if frnd[0].lower() == 'l':
        print(f'hey {frnd} ! ur name starts with L')
    else:
        print(f'hey {frnd} ! nice to see ya')
print('\n')
