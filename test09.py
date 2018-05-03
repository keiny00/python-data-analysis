before = ['2019', '12', '31']

after = list(map(int,before))

print(after)

for i in range(0,len(before)) :
    after[i] = int(before[i])

print(after)
