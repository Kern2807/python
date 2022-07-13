def fib(t):
    a = 0
    b = 1
    if t == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,t):
            c = a + b
            a = b
            b = c
            print(c)

fib(100)
