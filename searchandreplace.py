search_text = "Cheese"

replace_text = "Elephants"

with open(r'cheese.txt', 'r') as file:

    data = file.read()

    data = data.replace(search_text, replace_text)


with open(r'cheese.txt', 'w') as file:

    file.write(data)

print("Text replaced = ", data)
