cube = lambda x: x ** 3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

n = int(input())
fib = list(map(cube, [fibonacci(i) for i in range(n)]))
print(fib)
