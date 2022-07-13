rep = input('What word do you want to replace?')

rep_text = input('What word do you want to replace it with?')

search_text = rep

replace_text = rep_text

with open(r'party.txt', 'r') as file:

    data = file.read()

    data = data.replace(search_text, replace_text)


with open(r'party.txt', 'w') as file:

    file.write(data)

print("Text replaced = ", data)
