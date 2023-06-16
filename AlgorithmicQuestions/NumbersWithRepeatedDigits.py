def FindRepeatedDigits(num):

    repeateds = 0

    while True:
        num = str(num)
        length = len(num) -1
        for i in range(0,length):
            if num[i] == num[i+1]:
                repeateds += 1
            
        num = int(num)
        num -= 1
        num = str(num)

        if num == "0":break
    
    return repeateds


while True:
    flag = 1
    try:
        x = int(input("Sayi:"))
    except ValueError:
        print("Sayi girmeniz gerekmektedir\n")
        flag = 0
    if flag == 1:
        if x<=0:
            print("Pozitif bir sayi girmelisiniz!!!")
            flag = 0
        else:
            break

print("Tekrar sayisi =",FindRepeatedDigits(x))
