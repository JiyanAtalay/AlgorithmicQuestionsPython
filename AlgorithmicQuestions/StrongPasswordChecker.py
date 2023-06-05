from time import sleep
def StrongPassword(x):

    length = len(password)

    s = []

    if not 6 <= length <=20:
        s.append("Sifreniz en az 6 en fazla 20 karakter icermelidir")
    low , up , num = False,False,False

    if any('a' <= i <= 'z' for i in password):low = True
    else: s.append("Sifrenizde kucuk harf bulunmalidir")
    if any('A' <= i <= 'Z' for i in password): up = True
    else : s.append("Sifrenizde buyuk harf bulunmalidir")
    if any(i.isdigit() for i in password): num = True
    else : s.append("Sifrenizde rakam bulunmalidir")

    

    for i in range(2,length):
        if password[i] == password[i-1] == password[i-2]:
            s.append("Sifrenizde arka arkaya 3 karakter ayni olmamalidir")
            break

    sleep(1)
    print("\n")
    for i in range(0,len(s)):
        print(s[i])
    

    





while(True):
    password = input("Sifrenizi giriniz:")
    if any(i == ' ' for i in password):
        print("Sifreniz bosluk icermemelidir")
        sleep(0.65)
    else:
        break

StrongPassword(password)