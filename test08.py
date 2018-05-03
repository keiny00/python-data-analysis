# sting test


ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'

print(ss.count('공부')) # 공부 단어가 몇번 나왔는지 체크
print(ss.find('공부')) # 공부 단어가 문장의 몇번째 등장하는지 체크
print(ss.find('공부',5)) # 공부 단어가 문장의 5번째 이후에서 몇번째에 나왔는지 체크
print(ss.rfind('공부')) # 공부 단어가 문장의 뒤에서부터 몇번째인지 체크
print(ss.rfind('없다')) # 없다 단어가 문장에 몇번째 등장하는지 체크

print(ss.index('공부')) 
print(ss.rindex('공부'))
print(ss.index('공부', 5))

print(ss.startswith('파이썬'))
print(ss.startswith('파이썬', 10))
print(ss.endswith('^^'))

ss = '  파   이   썬   '

print(ss.strip())
print(ss.rstrip())
print(ss.lstrip())
sss = []
sss.append('(')
if ss.startswith('(') == False :
    for i in range(1,len(ss)+1) :
        sss.append(ss[i-1])

if ss.endswith(')') == False :
    sss.append(')')
    

print(sss)
#print(''.join(sss)) 

        


