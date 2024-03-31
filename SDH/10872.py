N = int(input())

def factorial(k):
    result = 1
    for i in range(1,k+1):
        result = result * i 
    return result

print(factorial(N))
