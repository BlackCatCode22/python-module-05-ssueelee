fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

for lin in hand:
    lin = lin.rstrip()
    print(lin)