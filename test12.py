def para_func (*para) :
    result, i = 0, 0
    for num in para :
        result += num
        i = i+1
    print("매개변수가 %d개인 함수를 호출한 결과 ==> %d" %(i, result))
    return result


hap = 0

hap = para_func(10,20,30,40,50,60,70)

    
