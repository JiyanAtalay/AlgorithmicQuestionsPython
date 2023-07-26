def superpalindromesInRange(left, right):
    def FindPalindromic(n):
        num = n
        kalan = 0
        ters = 0

        while num>0:
            kalan = num%10
            ters = ters*10 + kalan
            num = int(num/10)
        
        if ters == n:return True
        else:return False

    
    array = list()
    for i in range(left,right):
        if FindPalindromic(i) and FindPalindromic(i*i):
            array.append(i)
    return array

left = int(input("Baslangic:"))
right = int(input("Bitis:"))

x = superpalindromesInRange(left,right)
xx = list()

for i in x:
    xx.append(i*i)

print("Girdiginiz sayilar arasindaki super palindromlar =",superpalindromesInRange(left,right))
for i in range(len(xx)):
    print(x[i] , "=" , xx[i])
