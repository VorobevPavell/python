""" К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров. В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого автомобиля.

Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж. В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж. """

import json
count = []
d = {}
with open('manager_sales.json') as file:
   data = json.load(file)
for item in data:
   print(item['manager']['first_name'],item['manager']['last_name'])
   for car in item['cars']:
      count.append(car['price'])
   print(sum(count))
   d[sum(count)] = (item['manager']['first_name'],item['manager']['last_name'])
   count = []

print(*d[max(d.keys())],max(d.keys()))




