def FindOne(num:int):
    ones = 0
    
    while True:
        num = str(num)
        length = len(num)

        for j in range(0,length):

            if num[j-1] == "1":
                ones+=1

        num = int(num)
        num -= 1
        num = str(num)
        
        if num == "0":
            break

    return ones


while True:
    flag = 1
    try:
        x = int(input("Sayi:"))
    except ValueError:
        print("Sayi girmeniz gerekmektedir\n")
        flag = 0
    if flag == 1:break


print("Girdiginiz karaktere kadar olan 1 sayisi =",FindOne(x))
