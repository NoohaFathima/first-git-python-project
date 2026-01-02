skz_aliases = {
    "Bangchan": "Wolf Chan",
    "Lee Know": "Leebit",
    "Changbin": "Dwaekki",
    "Hyunjin": "Jiniret",
    "Han": "Han Quokka",
    "Felix": "BbokAri",
    "Seungmin": "PuppyM",
    "Jeongin": "FoxI.Ny"
}
for x,y in skz_aliases.items():
    print(f'{x} is also known as {y}')
print('\n\n\ skz dorm tracker\n')

#------------SKZ DORM ROOM TRACKER-------------

dorms={
    'dorm a':{
        'Felix':{
            'room':101,
            'snack':'brownie'
        },
        'Hyunjin':{
            'room':102,
            'snack':'kimchijigae'
        }
    },
    'dorm b':{
        'LeeKnow':{
            'room':104,
            'snack':'steak'

        },
        'Han':{
            'room':105,
            'snack':'candy'
        }

    }
}
print(dorms['dorm a']['Felix']['room'])
print(dorms['dorm b']['Han']['snack'])
print('\n')
dorms['dorm a']['IN']={
    'room': 103,
    'snack':'candy'
}
print(dorms)
print('\n')
dorms['dorm a']['Hyunjin'].update({'snack':'stew'})
print(dorms['dorm a']['Hyunjin'])
print('\n')
del dorms['dorm a']['IN']
print(dorms)
print('\n\n\LOOPING\n')

#-------------LOOOOOOOP-------------------

for dorm,members in dorms.items():
    print(f'\n{dorm.upper()} MEMBERS:')
    for name,info in members.items():
        print(f'{name} stays in {info['room']} and loves {info['snack']}')