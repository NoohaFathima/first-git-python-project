def myqoute():
    print('Can a heart still break once it has stopped beating?')


myqoute()
print('\n')


def shareqoute(line):
    print(line)


shareqoute('hi')
print('\n')


def shareqoute(name, quote):
    print(f'{name} once said: {quote}')
    shareqoute('leeknow', 'ICECREAAAAM')
    shareqoute('hyunjin', 'americanoo,johajoha')
    shareqoute('changbin', 'listen to my hearttu beattu')


def multiplynum(a, b):
    print(a*b)


multiplynum(4, 7)


def math_operation(a, b, operation):
    if operation == 'add':
        print(a+b)
    elif operation == 'multiply':
        print(a*b)
    else:
        print('unknown operation')


math_operation(7, 9, 'multiply')


def apple_cost(quantity):
    price = 10
    return quantity*price


totalprice = apple_cost(5)
print(totalprice)
print('\n')


def doubleword(word):
    return len(word)*2


result = doubleword('hello')
print(result)
print('\n')

vowels = ['a', 'e', 'i', 'o', 'u']


def secretcode(code):
    secret = ' '
    for letter in code:
        if letter in vowels:
            secret += '*'
        else:
            secret += letter
    return secret


secret = secretcode('hello')
print(secret)
print('\n')

# Default parameters--------------------


def introduce(name='Nooha', bias='felix'):
    print(f'HI! Im {name} and my SKZ bias is {bias}')


introduce()
# adding a 3rd default parameter to 'introduce'


def introduce(name='Nooha', bias='Felix', mood='to DO IT'):
    print(f'HI! Im {name},my SKZ bias is {bias} and Im feeling {mood}')


introduce()
introduce(bias='lee know')  # updating bias to 'lee know'


def remindme(task='breathe and listen to SKZ', time='now', mood='soft and fluffy'):
    print(f'Reminder: {task} - do it {time}, feeling {mood}')


remindme('learn math', 'at 7 pm', 'not so well')


def newline():
    print('\n\n')


newline()
print('skz les gooo')

newline()

nums = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x**2, nums))
print(squares)
newline()

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

newline()

fruits = ['apple', 'banana', 'cherry', 'grape', 'mango']

len_fruits = sorted(fruits, key=len)
print(len_fruits)

animals = ['dog', 'cat', 'elephant', 'ferret']

frst_letter = list(map(lambda x: x[0], animals))

print(frst_letter)

words = ['love', 'elegant', 'pretty', 'sad', 'map']

long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)

last_letter = sorted(fruits, key=lambda x: x[-1])
print(last_letter)

odd_doubled = list(map(lambda x: x*2 if x % 2 != 0 else x, nums))
print(odd_doubled)

names = ["Alice", "Bob", "Eve", "Uma"]
vowel_letter = list(filter(lambda x: x[0].lower() in 'aeiou', names))
print(vowel_letter)

tpl = [(1, 5), (2, 3), (4, 1)]

tpl2nd = sorted(tpl, key=lambda x: x[1])
print(tpl2nd)
