# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] =+ 1
#         else:
#             counts[word] = 1
#
#     return counts
#
# print( word_count(open('cheese.txt','r')))

file = open("cheese.txt","r")
counts = dict()
for line in file:
    words = line.split(" ")
    #print(words)
    #counts += len(words)
    for line2 in words:
        #print(line2)
        if line2 in counts:
            counts[line2] += 1
        else:
            counts[line2] = 1

print(counts)
