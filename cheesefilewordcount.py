
file = open("cheese.txt","r")
count = 0
for line in file:
    words = line.split(" ")
    print(words)
    count += len(words)

print("Number of words in these two paragraphs are:", count)
