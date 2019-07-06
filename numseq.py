#Fibonacci
from numseq.fib import fib

print ("Fibonacci")
for i in range(10):
    print ("{}: {}".format(i, fib(i)))
    
    
#Geo
from numseq.geo import *

print("Geometric numbers (square, triangle, cube)")
for i in range(10):
    print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

    
#Primes
from numseq.prime import *

print ("Primes")
prime_list = primes(1000)
for p in prime_list[-10:]:
    print (p)
print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))

