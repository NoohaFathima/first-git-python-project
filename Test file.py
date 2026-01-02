members = [
    ['chan', 'wolfchan', '🐺'],
    ['lee know', 'leebit', '🐈'],
    ['changbin', 'dweakki', '🐖🐇'],
    ['hyunjin', 'jiniret', '🥟'],
    ['han', 'hanqoukka', '🐿'],
    ['felix', 'bbokari', '🐥'],
    ['seungmin', 'puppym', '🐶'],
    ['in', 'foxy.in', '🦊']
]
emojidict = {m[0]: m[2]for m in members}
for name, emoji in emojidict.items():
    print(name.title(), emoji)
print('\n\nNICKNAME FILTER DICTIONARY\n')

# -------------NICKNAME FILTER DICTIONARY-----------------

filtered_nicks = {m[0]: m[1] for m in members if m[1].endswith(("a", "i"))}
for name, skzoo in filtered_nicks.items():
    print(name.title(), '-', skzoo)


nicknames = ['wolfchan', 'leebit', 'dweakki', 'jiniret',
             'hanqoukka', 'bbokari', 'puppym', 'foxy.in']
length_dict = {nickname: len(nickname)for nickname in nicknames}
for name, num in length_dict.items():
    print(name.title(), ':', num)


digitsum = {num: sum(int(d) for d in str(num)) for num in range(10, 31)}
print(digitsum)

codes = ['blink', 'stay', 'felix', 'stray', 'hyunjin', 'wolf', 'jiniret']
power_dict = {word: sum(ord(c)-96 for c in word) for word in codes}
print(power_dict)


for i in range(6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
