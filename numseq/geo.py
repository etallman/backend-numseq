# Geo
'''Within the numseq package, create a module named geo. Within the geo module, define 3 functions: square(n), triangle(n), and cube(n)'''
def square(n):
    for i in range(0, n):
        return n * n

#After being stuck, I moved onto the next lesson and found the solution.
def triangle(n):
        
        result=0
        for i in range(1, n):
                result = i * (i+1) / 2
                
        return result
       


def cube(n):
    for i in range(0, n):
        return n * n * n