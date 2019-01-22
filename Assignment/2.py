names = ['ViditShah', 'ArjunSharma', 'ram']
for name in names:
    if((len(name) > 5) and ('N' in name or 'n' in name)):
        print("Length of ", name, "is :", len(name))


while len(names) > 1:
    print(names.pop())
