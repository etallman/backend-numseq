# Geo
'''Within the numseq package, create a module named geo. Within the geo module, define 3 functions: square(n), triangle(n), and cube(n)'''
def square(n):
    for i in range(0, n):
        return i * i


def triangle(n):
        result=0
        for i in range(1, n):
                if i > 1:
                        next_i = i + 1
                        result = next_i + (i + 1)
                else:
                        next_i = i + 1
                        result = i + next_i
        return result


def cube(n):
    for i in range(0, n):
        return i * i * i