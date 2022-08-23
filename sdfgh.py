def fibonacci(n):
    term1, term2 = 0, 1
    if n == 1:
        print(term1)
    else:
        for i in range(0, n+1):
            print(term1)
            temp = term1 + term2
            term1 = term2
            term2 = temp
print(fibonacci(1))
