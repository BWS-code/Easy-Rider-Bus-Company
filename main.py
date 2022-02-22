import json
from collections import defaultdict, Counter

data = json.loads(input())
freq_dict = defaultdict(list)

search = 'bus_id'
for element in data:
    for k, v in element.items():
        if k == search:
            freq_dict[k].append(v)

count = Counter(freq_dict['bus_id'])

print('Line names and number of stops:')
for k, v in count.items():
    print(f'{search}: {k}, stops: {v}')
    
------------------OR---------------------

import json
from collections import defaultdict, Counter


data = json.loads(input())
search = 'bus_id'

count = Counter([v for element in data for k, v in element.items() if k == search])
print('\n'.join(f'{search}: {k}, stops: {v}' for k, v in count.items()))
