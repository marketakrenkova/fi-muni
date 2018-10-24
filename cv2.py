def divisors(n):
    "print all divisors of number n"
    for i in range (1, n + 1):
        if n % i == 0:
            print(i)

def divisors_count(n):
    "return count of divisors of number n"
    count = 0
    for i in range (1, n + 1):
        if n % i == 0:
            count += 1
    return count

def is_prime(n):
    "return true if n is prime"
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

            
        
            
            
                
                
                    
                
                    
                
               
                
  
            
        
        
