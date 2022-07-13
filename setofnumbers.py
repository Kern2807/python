import random

number = random.sample(range(1,100),13)

for i in range(len(number)):

  for j in range(i+1,len(number)):
      print(number)

      if number[i]>number[j]:
          
          number[i],number[j]=number[j],number[i]

print(number)

x = input()
