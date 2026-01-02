num=456
guessed=False
print('\nWELCOME TO THE NUMBER GUESSING GAME !\n\nRULES:')
print('* you get 5 tries\n' \
'*each time you will get a hint\n' \
'* only numbers between 0-999\n' \
'*at last, enjoy! <3\n')
if not guessed:
    guess1=int(input('GUESS NO 1 : (No hints for this one just pure guess :) )'))
    if guess1==num:
        print('corrrect on the first try')
        guessed=True
    else:
        print('no luck i guess is ok lets move on\n')
if not guessed :
    guess2=int(input('GUESS NO 2 (HINT: its a three digit num) :'))
    if guess2==num:
        print('and thats correct ')
        guessed=True
    else:
        print('im sorry but no try again\n')
if not guessed:
    guess3=int(input('GUESS 3 : (HINT: Its under 500) :'))
    if guess3==num:
        print('3rd times is actually a charm ! and u are right')
        guessed=True
    else:
        print('oops wrong 3rd times a charm doesnt actually work i guess\n')
if not guessed:
    guess4=int(input('GUESS NO 3 : (HINT : its starts with 4 )'))
    if guess4==num:
        print('u got it ')
        guessed=True
    else:
        print('noooo u got it wrong ..last chance\n')
if not guessed:
    guess5=int(input('UR FINAL GUESS:(HINT: think squid game..this is a very big hint)'))
    if guess5==num:
        print('YYEEEEES U GOT IT !')
        guessed=True
    else:
        print('how can u not get it after that hint..u really are stupid u lose..the answer is',num)
print('\nthank u for playing\n')
print(input('press entr to exit:'))


