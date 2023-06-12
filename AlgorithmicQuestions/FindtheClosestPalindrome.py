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

if FindPalindromic(x):
    print(x)
    exit()

up = 0
down = 0
xd = x
xu = x

while True:
    xd = xd - 1
    down += 1
    if FindPalindromic(xd):
        break

while True:
    xu = xu + 1
    up += 1
    if FindPalindromic(xu):
        break


if up<down:
    print(xu)
else:
    print(xd)

    