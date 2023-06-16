#The number 197 is called a circular prime because all rotations of the digits:197,971 and 719 are themselves prime.
#How many circular primes are there below 100.000?

#197 tum donusumleri asal oldugu icin dairesel asal olarak adlanıdırılır:197,971 ve 719 donusumlu asallardir.
#100.000'den kucuk kac tane dairesel asal sayi vardir?

def FindCircularPrimes():
    def FindPrime(x):
        if x<0 or x == 0 or x == 1:
            return False
        elif x == 2:
            return True
        for i in range(2,x):
            if x%i == 0:
                return False
        return True
    
    CircularPrimes = [2,3,5,7]

    for i in range(10,100):
        if FindPrime(i):
            a = int(i/10)
            a += (i%10)*10
            if FindPrime(a):
                CircularPrimes.append(a)
    for j in range(100,1000):
        if FindPrime(j):
            b = (j%100)*10
            b += int(j/100)
            c = (b%100)*10
            c += int(b/100)
            if FindPrime(b) and FindPrime(c):
                CircularPrimes.append(j)
    for k in range(1000,10000):
        if FindPrime(k):
            d = (k%1000)*10
            d += int(k/1000)
            e = (d%1000)*10
            e += int(d/1000)
            f = (e%1000)*10
            f += int(e/1000)
            if FindPrime(d) and FindPrime(e) and FindPrime(f):
                CircularPrimes.append(k)
    for l in range(10000,100000):
        if FindPrime(l):
            g = (l%10000)*10
            g += int(l/10000)
            h = (g%10000)*10
            h += int(g/10000)
            m = (h%10000)*10
            m += int(h/10000)
            n = (m%10000)*10
            n += int(m/10000)
            if FindPrime(g) and FindPrime(h) and FindPrime(m) and FindPrime(n):
                CircularPrimes.append(l)
    CircularPrimes.sort()
    print(CircularPrimes)




FindCircularPrimes()


    

