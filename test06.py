import operator as op

ss = "sadjkhfdkgdfmsnckahdokfnkdngkdnafkjnadgjkdfngkdajgkwjeiuriewqelaspoqelqdlaafdfmdsgmfdamhlkmgakaj"
print(ss)
a = {}

for i in ss :
    if i not in a :
        a[i] = 1
    else :
        a[i] += 1

print(a)

b = sorted(a.items(), key = op.itemgetter(1))

for i in b :
    print(i[1], i[0])

print('\n')

c = sorted(a.items(), key = op.itemgetter(0))

for i in c :
    print(i[0], i[1])
    
