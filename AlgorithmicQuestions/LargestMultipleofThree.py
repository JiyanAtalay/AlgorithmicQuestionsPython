def largestMultipleOfThree(nums:list[int]):
    nums.sort()
    
    toplam = sum(nums)
    x = 0
    if toplam%3 == 0:
        length = len(nums)
        for i in range(length-1,-1,-1):
            x += nums[i]*(10**i)
        print("Girdiginiz rakamlardan olusup 3'e bolunmeyen en buyuk sayı =",x)
    elif toplam%3 == 1:
        flag2 = 0
        flag22 = 0
        deletes = []
        for j in nums:
            if j%3 == 1:
                deletes.append(j)
                flag2 += 1
                break
        if flag2 != 1:
            for n in nums:
                if n%3 == 2:
                    deletes.append(n)
                    flag22 += 1
                    if flag22 == 2:
                        break
        for g in deletes:
            nums.remove(g)

        length = len(nums)
        for i in range(length-1,-1,-1):
            x += nums[i]*(10**i)
        print("Girdiginiz rakamlardan olusup 3'e bolunmeyen en buyuk sayı =",x)

    elif toplam%3 == 2:
        flag3 = 0
        flag32 = 0
        deletes2 = []
        for s in nums:
            if s%3 == 2:
                deletes2.append(s)
                flag3 += 1
                break
        if flag3 != 1:
            for l in nums:
                if l%3 == 1:
                    deletes2.append(l)
                    flag32 += 1
                    if flag32 == 2:
                        break
        for z in deletes2:
            nums.remove(z)

        length = len(nums)
        for b in range(length-1,-1,-1):
            x += nums[b]*(10**b)
        print("Girdiginiz rakamlardan olusup 3'e bolunmeyen en buyuk sayı =",x)

    

    



k = 1
array = []
print("Eleman eklemeyi durdurmak icin 'q'ya basiniz\nSadece rakam giriniz!!")


while True:
    x = input("{}.eleman :".format(k))

    if x == "q":
        break
    
    flag = 1

    try:
        x = int(x)
    except ValueError:
        print("Sayi girmeniz gerekmektedir!")
        flag = 0
    
    if flag == 1:
        k += 1
        array.append(x)


largestMultipleOfThree(array)

