members = [
    ['chan','wolfchan','🐺'],
    ['lee know','leebit','🐈'],
    ['changbin','dweakki','🐖🐇'],
    ['hyunjin','jiniret','🥟'],
    ['han','hanqoukka','🐿'],
    ['felix','bbokari','🐥'],
    ['seungmin','puppym','🐶'],
    ['in','foxy.in','🦊']
]
for member in members:
    print(member[0].title(),'-',member[1])
print('\n\n SKZoo profile\n')
for member in members:
    print(member[0].title(),'-',member[1].title(),member[2])
print('\n\nSKZoo emoji filter\n')

emoji=input('enter emoji to filter by:')
found=False
for member in members:
    if member[2]==emoji:
        print(member[0].title(),'-',member[1].title(),member[2])
        found=True
if not found:
    print ('invalid emoji')
print('\n\n list comprehension:creating a list only with emojis\n')

skz_emojis=[member[2] for member in members]
print(skz_emojis)
# list comprehension : newlist= expression for item in originallist if condition
print('\n\nSKZoo bias tracker\n')
nameinput=input('enter name of the member ')
matches=[member for member in members if member[0]==nameinput]
if matches:
    for match in matches:
        print(match[0].title(),match[1].title(),match[2])
else:
    print('not in the archive')
print('\n\nskzoo emoji count\n')

multipleemojis=[member for member in members if len(member[2])>1]
count=0
if multipleemojis:
    for multipleemoji in multipleemojis:
        count+=1
        print(count)
        print(multipleemoji[0].title(),multipleemoji[1].title(),multipleemoji[2])
print('\n\nSKZoo alias length filter\n')

skzoonames=[member for member in members if len(member[1])>7]
if skzoonames:
    for skzooname in skzoonames :
        print('skzoo with more than 7 charecters:',skzooname)

print('total members:',len(members))
for member in members:
    print(member)
