def countOperationsToEmptyArray(nums:list[int]):

    i = 0
    while True:
        length = len(nums)

        if length == 0:
            break
        
        if length == 1:
            nums.remove(nums[i])
            print(nums)

        elif nums[i] > nums[i+1]:
            a = nums[i]
            nums.remove(nums[i])
            nums.append(a)
            print(nums)
        
        else:
            nums.remove(nums[i])
            print(nums)



k = 1
array = []
print("Eleman eklemeyi durdurmak icin 'q'ya basiniz")


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
        
print(array)
countOperationsToEmptyArray(array)
