# hacer un programa que calcule el triangulo de pascal 
"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""

def factorial(num):
    fact = 1
    for n in range(2, num+1):
        fact*=n
    return fact

print(factorial(5))

def combinatoria(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))


def triangulo_Pascal(p):
    for n in range(p+1):
        for k in range(n+1): 
            res= combinatoria(n,k)
            print(res, end="\t")
        print()

triangulo_Pascal(3)
        
        