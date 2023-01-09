import json
d = []
with open('group_people.json') as file:
    data = json.load(file)

    for item in data:
        count = 0
        print('group = ',item['id_group'])
        for people in item['people']:
            if people['gender'] == 'Female' and people['year'] > 1977:
                count += 1
        d.append(count)


id_group = d.index(max(d)) + 1 
print(id_group,max(d))