def InttoRoman(num):
    romanNums = {
        500000: 'D',
        100000: 'C',
        50000: 'L',
        10000: 'X',
        5000: 'V',
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman = ''
    for value, symbol in romanNums.items():
        while num >= value:
            roman += symbol
            num -= value

    return roman

sayi = int(input("Bir tam sayı girin: "))
Roman = InttoRoman(sayi)

print("Roma rakamı:", Roman)

