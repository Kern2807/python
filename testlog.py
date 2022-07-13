base = int(input("Enter a number for the base:"))
num = int(input("Enter a number for the argument:"))

for i in range(1000):
    print(i)
    y = base**i
    if y == num:
        print("log is", i)
        break
    elif y > num:
        print("log is between", i-1, "and", i)
        break
