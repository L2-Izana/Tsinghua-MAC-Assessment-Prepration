import sys 
import math

def solve():
    input = sys.stdin.read().strip().split()
    n, m = int(input[0]), int(input[1])
    if math.gcd(n, m) > 1: # not coprime
        print(0)
        return 
    # k is the order of n in number theory
    sqrt_n = math.sqrt(n)
    euler_totient = old_euler_totient(n)
    print(euler_totient)
    for i in range(2, euler_totient+1):
        if euler_totient % i == 0:
            if (m ** i - 1) % n == 0: # This is the order of n, or the smallest number that m^k = 1 module n
                print(i)
                return
    print(0)
def is_prime(num):
    sqrt_n = math.sqrt(num + 1) # Wrong, can be wrong if n is a power of primes, e.g., 4. Plus 1 is safer
    for i in range(2, math.floor(sqrt_n)):
        if num % i == 0:
            return False
    return True 
def old_euler_totient(num):
    euler_totient = num
    # This is wrong as Ertosthenes sleve is for CHECKING if a number is a prime, not to find all the prime divisors, e.g. you will miss 11 in 77 => Need to loop all
    for i in range(2, num+1):
        if num % i == 0 and is_prime(i):
           euler_totient = euler_totient * (i - 1) // i
    return euler_totient
def faster_euler_totient(num):
    # Like before, but try to decrease n maximally when looping through p
    euler_totient = num
    p = 2
    while p * p <= num:
        if num % p == 0:
            # This is the smartest thing I have ever seen :), don't check is_prime for every number, instead, as we delete all p^s from num, all number that is divided by p will be neglected
            while num % p == 0: # As we only counter the prime divisor once so remove all the p from n 
                # Interestingly, this is safe even we decreases the search space as numerically, 
                num //= p
            euler_totient-=euler_totient//p # This is brilliant, we compute n(1-1/p) incrementally as n(1-1/p)(1-1/q)=n'(1-q) where n' = n - n/p
        p+=1
    # Similarly to the bug of Ertosthenes above, we can still miss 11 from 77
    if num > 1:
        euler_totient-=euler_totient//num # A number can have at most ONE prime factor that is greater than it's sqrt, can be easily proven
    return euler_totient
solve()
