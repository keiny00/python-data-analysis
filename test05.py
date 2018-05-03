""" # list
money = 0;
coin_class = ['500', '100', '50', '10']
coin_number = [0, 0, 0, 0]

money=int(input("교환할 돈은 얼마 ? "))
print("\n")

for i in range(0,len(coin_class),1) :
    coin_number[i] = money // int(coin_class[i])
    money %= int(coin_class[i])
    print("%s원원 짜리 ==> %d개" % (coin_class[i], coin_number[i]))
print("바꾸지 못한 잔돈 ==> %d원" % money) """

# dictionary
money = 0;
coin = { 500 : 0, 100 : 0, 50 : 0, 10 : 0}

money=int(input("교환할 돈은 얼마 ? "))
print("\n")

for k in coin.keys() :
    coin[k] = money // k
    money %= k
    print("%s원 짜리 ==> %d개" % (k, coin[k]))
print("바꾸지 못한 잔돈 ==> %d원" % money) 

