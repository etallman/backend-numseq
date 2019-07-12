# Fibonacci
'''Within the numseq package, creates a module named fib. Within the fib module, defines a function fib(n) that returns the nth Fibonacci number.'''


def fib(n):
    fib_list = [0,1]
    
    for i in range(2, n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-1])

    return fib_list[n]