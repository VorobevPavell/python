from datetime import datetime
import json
from random import randint
str_json = '''
{
  "result": {
    "Campaigns": [{
      "Name": "Test API Sandbox campaign 1",
      "Id": 1234567
    }, {
      "Name": "Test API Sandbox campaign 2",
      "Id": 1234578
    }, {
      "Name": "Test API Sandbox campaign 3",
      "Id": 1234589
    }]
  }
}
'''

data = json.loads(str_json)
for item in data['result']['Campaigns']:
    item['likes'] = randint(100,200)
    item['get_for_del'] = randint(500,700)
    del item['get_for_del']
    item['TESTTTTT'] = 'test'
    item['now'] = datetime.now().strftime('%y/%m/%d')
new_json = json.dumps(data,indent=2)
with open('my_json','w') as f:
    json.dump(data,f,indent=3)

with open('my_json','r') as f2:
    data2 = json.load(f2)

print(data2)