for x in range(6):
    for i in range(5):
        print('<3',end='  ')
    print('')
print('\n\n LALALALALALALALALALALALALALLALALALA\n')

for i in range(6):
    for j in range(0,i+1):
        print('*',end='')
    print('')
print('\n\n')

for i in range( 0,9):
    for j in range(i,0,-1):
        print(j,end='')
    print('')
print('\n')

for i in range(7):
    print('*'*i)
for j in range(5,0,-1):
    print('*'*j)
print('\n')
evencount=0
oddcount=0
for i in range(21):
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
print('no of odds:',oddcount,'\n'
    'no of evens:',evencount)
print('\n')
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

#-----------------------------#
count=0
vowels=['a','e','i','o','u']
word=input('enter a word: ').lower()
for letter in word:
        if letter in vowels:
            count+=1
print(count)
print('\n')

#--------------------------------------------#

sentence=input('enter a sentence: ')
words=sentence.split()
words_counts={}
for word in words:
    words_counts[word]=len(word)
print(words_counts)
