import json
with open('Alphabet.json') as file:
    data = json.load(file)

st = ''
with open('Abracadabra__1_.txt','r') as file2:
    for line in file2:
        for letter in line:

            if letter in data:
                letter = data[letter]
            else:
                letter = letter
            st += letter
print(st)