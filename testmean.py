import random

print("")

t = int(input("Please enter the number of terms you want:"))

print("")

g = int(input("Please enter the lowest number for the range:"))

print("")

h = int(input("Please enter the highest number for the range:"))

print("")

num_list = [random.randint(g,h) for x in range(t)]

print("Unsorted list is", num_list)

print("")

total = 0

for num in num_list:

    total = total + num

print("Total is", total)

print("")

x = len(num_list)

print("Number of terms is", x)

print("")

mean = total / x

print("The mean is" ,mean)

print("")

l_ist = num_list

for i in range(len(l_ist)):

  for j in range(i+1,len(l_ist)):

    if l_ist[i]>l_ist[j]:

      l_ist[i],l_ist[j]=l_ist[j],l_ist[i]

print("Sorted list is", l_ist)

print("")

n = len(num_list)

if n % 2 == 0:
    median1 = num_list[n//2]
    median2 = num_list[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = num_list[n//2]

print("The median is" ,median)

print("")

m_ode = num_list

def frequent(m_ode):
    count = 0

    numb = m_ode[0]

    for x in m_ode:

        frequency = m_ode.count(n)

        if(frequency> count):

            count = frequency

            numb = x

    return num

print("The mode is" ,frequent(m_ode))

x = input()
