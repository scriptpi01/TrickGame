
raww = input().split()
raww1 = int(raww[0])
raww2 = int(raww[1])
test = []
for i in range(1):
    for i in range(raww1):
        x = [str(x) for x in input().split()]
        test.append(x)

hin = [int(h) for h in input().split()]
num = []
num[0:raww2] = hin[0:raww2]

for i in range(9999):
    if hin[0] == i:
        hin.remove(hin[0])
        hin.insert((0),('#'.split()*i))
    if hin[1] == i:
        hin.remove(hin[1])
        hin.insert((1),('#'.split()*i))
    if hin[2] == i:
        hin.remove(hin[2])
        hin.insert((2),('#'.split()*i))
    if hin[3] == i:
        hin.remove(hin[3])
        hin.insert((3),('#'.split()*i))
    if hin[4] == i:
        hin.remove(hin[4])
        hin.insert((4),('#'.split()*i))


print('------------------')
print(len(test))
print('------------------')

for i in range(8):
    for j in range(5):
        if test[i][0] == 'o':
            test[i-1:i-num[0]][0] = '#'
        else:
            pass



print('--------------------------')


for i in range(8):
    print(*test[i][0:5])
