#Fibonacci
'''Within the numseq package, creates a module named fib. Within the fib module, defines a 
function fib(n) that returns the nth Fibonacci number.'''
from numseq.fib import fib
print ("Fibonacci")
def fib(n):
    result = 0
    n1 = 0
    n2 = 1
    for num in range(0, n-2):
        result = add(n1, n2)
        n1 = n2
        n2 = result
    return result

    for i in range(10):
        print ("{}: {}".format(i, fib(i)))

    
#Geo
    '''Within the numseq package, create a module named geo. Within the geo module, define 3 functions: square(n), triangle(n), and cube(n)'''
    from numseq.geo import *
    print("Geometric numbers (square, triangle, cube)")
    def square(n):
        pass
    def triangle(n):
        pass
    def cube(n):
        pass

    for i in range(10):
        print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

    
#Primes
    '''Creates a module named prime within the numseq package. Defines the following functions: 1) primes(n) returns a list of all primes less than n and 2)
    is_prime(m) returns a boolean indicating whether m is a prime number.'''
    from numseq.prime import *
    print ("Primes")
    
    def primes(n):
        if n > 1:
            for i in range(1,n):
                if (n % i) == 0:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
    
#     def is_prime(m):
        
#     prime_list = primes(1000)
#     for p in prime_list[-10:]:
#         print (p)
# print ("Is 999981 prime? {}".format(is_prime(999981)))
# print ("Is 999983 prime? {}".format(is_prime(999983)))