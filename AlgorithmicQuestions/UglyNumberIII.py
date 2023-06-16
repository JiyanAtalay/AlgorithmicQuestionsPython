def nthUglyNumber(n,a,b,c):
    i = 1
    UglyNums = 0
    while True:
        if i%a == 0 or i%b == 0 or i%c == 0:
            UglyNums += 1
        if UglyNums>=n:
            break
        i += 1
    
    return i



nums = list()
for sira in [1,2,3]:
    while True:
        flag = 1
        try:
            x = int(input("{}.sayi:".format(sira)))
        except ValueError:
            print("Sayi girmeniz gerekmektedir\n")
            flag = 0
        if flag == 1:
            if x<=0:
                print("Pozitif bir sayi girmelisiniz!!!")
                flag = 0
            else:
                nums.append(x)
                break

while True:
    flag = 1
    try:
        n = int(input("Kacinci ugly number:"))
    except ValueError:
        print("Sayi girmeniz gerekmektedir\n")
        flag = 0
    if flag == 1:
        if n<=0:
            print("Pozitif bir sayi girmelisiniz!!!")
            flag = 0
        else:
            break
        
print("{}.ugly number = ".format(n),end="")
print(nthUglyNumber(n,nums[0],nums[1],nums[2]))