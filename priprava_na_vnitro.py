import math


def odd_numbers(n):
    "licha cisla"
    for i in range(n*2):
        if i % 2 != 0:
            print(i, end = " ")

def powers2(n):
    "mocniny 2"
    for i in range(n):
        print(2**i, end = " ")

def powers(n):
    "druhe mocniny"
    for i in range(n):
        print(i**2, end = " ")  #?jesti i 0 a 1?
            

def collatz_sequence(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    print(1)

def to_binary(number):
    n = number
    output = ""
    while n > 0:
        if n % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        n = n//2
    print(output)


def divisors_count(n):
    "return count of divisors of number n"
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def is_prime(n):
    return divisors_count(n) == 2

def primes(n):
    "prvocisla"             
    k = 0
    i = 2
    while k < n:
        if is_prime(i):
            print(i, end = " ")
            k += 1
        i += 1

def factorization(n):
    "prvociselny rozklad"
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i):
            print(i)
            n = n/i
            while n % i == 0:
                print(i)
                n = n/i

def power_factorization(n):
    "prvociselny rozklad v mocninach, napr.: 2^3 3^4)"
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i):
            power = 1
            n = n/i
            while n % i == 0:
                power += 1
                n = n/i
            print(i, end = "")
            print("^", end = "")
            print(power, end = " ")

def gcd(a,b):
    "nejvetsi spolecny delitel...naivne"
    maxd = 1
    if b < a:
        a,b = b,a
    for i in range (2, a+1):
        if a % i == 0 and b % i == 0:
            maxd = i
    return maxd

def lcm(a,b):
    "nejmensi spolecny nasobek"
    if b < a:
        a,b = b,a
    for i in range (a, (a*b)+1):
        if i % a == 0 and i % b == 0:
            return i

def e():
    i = 2
    sum_e = 2
    while 1/math.factorial(i) > 1/1000000:
        sum_e += 1/math.factorial(i)
        i += 1
    return round(sum_e,6)

def multiples(n):
    " 10 nasobku n"
    for i in range(1,11):
        print(n*i, end = "")
        if i < 10:
            print(",", end = " ")

def table_modulo(n):
    "table_modulo(n) vypíše tabulku s daným počtem řádků a sloupců, kde v každé buňce se nachází zbytek po dělení čísla sloupce číslem řádku."
    n_digit = 0
    n2 = n
    while n2 != 0:           #to know how to align the numbers
        n_digit += 1           #n_digit - number of digits
        n2 = n2 // 10
    print(n_digit*" ", end = "   ")
    for i in range(1, n+1):
        print (str(i).ljust(n_digit), end = " ")
    print()
    print(n_digit*" ", end = "   ")
    for i in range(n):
        print("-".ljust(n_digit), end = " ")
    print()
    for i in range(1, n+1):
        print (str(i).ljust(n_digit), end = " ")
        print("|", end = " ")
        for j in range(1, n+1):
            print(str(j % i).ljust(n_digit), end = " ")
        print()

def print_house(roof_height):
    number_of_space = roof_height - 1
    k = 0
    for i in range(roof_height-1):
        if i == 0:
            print("  "*number_of_space, end = "")
            print("#")
            number_of_space -= 1
        else:
            print("  "*number_of_space, end = "")
            print("#",(2*i - 1)*". ", end = "")
            print("#")
            number_of_space -= 1
            k += 1
        
    for i in range(2*roof_height - 1):
        if i == 0 or i == (2*roof_height - 2):
            for j in range(2*roof_height - 1): 
                print("#", end = " ")
            print()
        else:
            print("#", end = "")
            print((2*roof_height - 3)*"  ", "#")

def print_p(height, width):
    for i in range(1, height + 1):
        if i == 1 or i == (height // 2 + 1):
            print((width - 1)*"#")
        elif 1 < i < (height // 2 + 1):
            print("#", end = "")
            print((width - 2)*" ", end = "")
            print("#")
        else:
            print("#")        

