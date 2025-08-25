
def fact(n) :
    if n == 0 or n == 1 : return 1

    result = n * fact(n - 1)
    return result

result  = fact(5)
print(result)