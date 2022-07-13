def fib(t):
    a = 0
    b = 1
    c = b
    while c < t:
        c = a + b
        a = b
        b = c
        if c < t:
            print(c)

fib(100)
