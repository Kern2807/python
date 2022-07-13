base = int(input("Input a number for the base:"))


def dectobin(n):
   if n > 1:
       dectobin(n//base)
   print(n % base,end = '')



dec = int(input("Enter A Decimal Value:"))
print("Base value is:")
dectobin(dec)

print("")

bin = list(input("Enter A Base Value: "))
value = 0

for i in range(len(bin)):
    digit = bin.pop()
    if digit == '1':
        value = value + pow(base, i)
print("Decimal value is:")
print(value)

x = input()

print("Hope this helped with the calculations!")
