import math


def divisors_count(n):
    "return count of divisors of number n"
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def is_prime(n):
    return divisors_count(n) == 2
        

def factorization(n):
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i):
            print(i)
            n = n/i
            while n % i == 0:
                print(i)
                n = n/i

def power_factorization(n):
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

            
    
