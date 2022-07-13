number = int(input("Enter number"))
sum = 0

for num in range(1, number + 1, 1):

    sum = sum + num


average = sum / number

print("Average of ", number, "numbers is: ", average)