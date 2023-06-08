from time import sleep

nums1 = []
nums2 = []

i = 1
j = 1

print("Eleman eklemeyi durdurmak icin q'ya basiniz")

sleep(1)

while(True):
    x = input("1.dizinin {}.elemani:".format(i))

    if x == "q":
        break

    flag1 = 1

    try:
        x = int(x)
    except ValueError:
        print("Sayi girmeniz gerekmektedir")
        flag1 = 0
    
    if flag1 == 1:
        nums1.append(x)
        i += 1
    
sleep(1)
print("\n")
while(True):
    y = input("2.dizinin {}.elemani:".format(j))
    j += 1

    if y == "q":
        break

    flag2 = 1

    try:
        y = int(y)
    except ValueError:
        print("Sayi girmeniz gerekmektedir")
        flag2 = 0
    
    if flag2 == 1:
        nums2.append(y)

MergedNums = nums1 + nums2
MergedNums.sort()

if len(MergedNums)%2 != 0:
    z = len(MergedNums)/2
    z = int(z)

    print("Birlestirilmis dizi = ",MergedNums)
    print("Birlestirilmis dizinin medyani = ",MergedNums[z])

else:
    z1 = len(MergedNums)/2
    z2 = z1-1

    z1 = int(z1)
    z2 = int(z2)



    median = (MergedNums[z1]+MergedNums[z2])/2
    print("Birlestirilmis dizi = ",MergedNums)
    print("Birlestirilmis dizinin medyani = ",median)
    
