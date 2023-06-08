
arrayP = []
arrayN = []
i = 1

print("Eleman eklemeyi durdurmak icin 'q' ya basınız\n")

while True:
    x = input("{}.eleman :".format(i))
    
    if x == "q":
        break

    flag = 1

    try:
        x = int(x)
    except ValueError:
        print("Sayi girmeniz gerekmektedir!")
        flag = 0
    
    if flag == 1:
        i+=1
        if x < 0:
            arrayN.append(x)
        elif x > 0:
            arrayP.append(x)
        

arrayN.sort()
lengthN = len(arrayN)
lengthP = len(arrayP)

if lengthN%2 != 0:
    arrayN.remove(arrayN[-1])

Carpim = 1

for i in arrayP:
    Carpim *= i

for j in arrayN:
    Carpim *= j

print("En buyuk carpim =",Carpim)