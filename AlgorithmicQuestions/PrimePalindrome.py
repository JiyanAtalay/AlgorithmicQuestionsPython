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

def FindPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

flag = 1
while True:
    try:
        x = int(input("Sayi:"))
    except ValueError:
        flag = 0
        print("Sayi girmeniz gerekmektedir!!!\n")
    if x<=0:
        print("Pozitif deger girmeniz gerekmektedir!!!\n")
        flag = 0

    if flag == 1:
        break

if FindPalindromic(x) and FindPrime(x):
    print(x)
    exit()

while True:
    x += 1
    if FindPalindromic(x) and FindPrime(x):
        break


print("\nClosest Prime Palindrome =",x)