members = ['chan','leeknow','changbin','hyunjin','han','felix','seungmin','IN']
count=0
for name in members:
    if len(name)<=5:
        count+=1
        print('shor name alert!!', name)
    else:
        print('members:', name)
print("total shorties with short names:", count)
print('\n\nFanchant remix..but with skipping hanniee:\n')
#  Task1: short name count

# Task 2:Fnchat remix!!..but with skipping hannie :(
for name in members:
    if name=='han':
        continue
    elif  name=='felix':
        print('Felix Sunhine!!!!')
    else:
        print('Lets go', name +'!')
print('\n\nMembers position by using range\n')
# Task 3:get the members position with their range
for i in range(len(members)):
    print(f'Member{i+1}:{members[i]}')
print('\n\nreverse lineup\n')

# task 4: reverse lineup
for i in range (len(members)-1,-1,-1):
    print (f'Members{i+1}:{members[i]}')
print('\n\nmember match up with their roles(using zip)\n')

#Task 5: member match up with theri roles
roles = ["Leader", "Dancer", "Rapper", "Visual", "Lyricist", "Dancer", "Vocalist", "Maknae"]
for member,role in zip(members,roles):
    print(f'{member} is the {role}')
print('\n\n bias battle royale\n')

# task 6: Bias battle royale
biaspoints=[8,10,8,10,8,10,10,8]
for member,role,bias in zip(members,roles,biaspoints):
    if  bias==10:
        print(f'dangerous bias detected!! {member} is the{role} with bias level{bias}')
        
    else:
         print(f'{member} is the {role} with bias level  {bias}')
print('\n\n with emojis this time and a count\n')

# same task as 6 but with emojis and a bias count
biaspoints=[8,10,8,10,8,10,10,8]
count=0
for member,role,bias in zip(members,roles,biaspoints):
    if  bias==10:
        print(f'🔥dangerous bias detected!! {member} is the{role} with bias level{bias}💘 ')
        count +=1
    else:
         print(f'{member} is the {role} with bias level  {bias}')






    









    
