# for only

"""hap, i, a, b, c = 0,0,0,0,0

a = int(input("*** 첫 번째 숫자를 입력하세요 : "))
b = int(input("*** 두 번째 숫자를 입력하세요 : "))
c = int(input("*** 세 번째 숫자를 입력하세요 : "))       

for i in range(a,b+1,c) :
    hap += i

print('%d' % hap)"""


# for - if
    
"""hap, i, a, b, c = 0,0,0,0,0

a = int(input("*** 첫 번째 숫자를 입력하세요 : "))
b = int(input("*** 두 번째 숫자를 입력하세요 : "))
c = int(input("*** 세 번째 숫자를 입력하세요 : "))       

for i in range(a,b+c,1) :
    if (i-a) % c == 0 :
        hap += i
    

print('%d' % hap)"""

# for - if - continue

"""hap, i, a, b, c = 0,0,0,0,0

a = int(input("*** 첫 번째 숫자를 입력하세요 : "))
b = int(input("*** 두 번째 숫자를 입력하세요 : "))
c = int(input("*** 세 번째 숫자를 입력하세요 : "))       

for i in range(a,b+c,1) :
    if (i-a) % c != 0 :
        continue
    hap += i"""
    

print('%d' % hap)

