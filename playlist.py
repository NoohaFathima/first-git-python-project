playlist=[]
print('welcome to ur playlist<3')
while True:
    action=input('do you want to add,pop,insert,remove a song,view ur playlist or quit?').lower()
    if action=='add':
        song=input('enter the song u wanna add: ')
        playlist.append(song)
        print(song,'added to ur playlist')
        
    elif action=='remove':
        song=input('enter song u wanna remove: ')
        if song in playlist:
            playlist.remove(song)
            print(song,'is removed from ur playlist')
        else:
            print(song,'not found')
            
    elif action=='insert':
        song=input('enter song u wanna insert:')
        index=int(input('enter index'))
        playlist.insert(index,song)
        print(song ,'is inserted at', index)
        
    elif action=='pop':
        index=input('enter index u wanna pop(or press enter to pop the last song)')
        if index in playlist:
            if index:
                poppedsong=playlist.pop(int(index))
            else:
                poppedsong=playlist.pop()
            print(poppedsong,'is popped from ur playlist')
        else:
            print('index out of range')

        
    elif action=='view':
        print('here is ur current playlist <3 : ',playlist)
    elif action=='quit':
        print('goobyee see u next time <3')
        break
    else:
        print('invalid command')
        
        
        
