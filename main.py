import json
import re
from collections import defaultdict

data = json.loads(input())
err_dict = defaultdict(int)

check_list = {
    'bus_id': {
        'data': int,
        'mandatory': True,
        'format': None
    },
    'stop_id': {
        'data': int,
        'mandatory': True,
        'format': None
    },
    'stop_name': {
        'data': str,
        'mandatory': True,
        'format': '^[A-Z]\w+\s.*?(Road|Boulevard|Street|Avenue)$'
    },
    'next_stop': {
        'data': int,
        'mandatory': True,
        'format': None
    },
    'stop_type': {
        'data': str,
        'mandatory': False,
        'format': '^[SOF]?$'
    },
    'a_time': {
        'data': str,
        'mandatory': True,
        'format': '^(0\d|1\d|2[0-3]):[0-5]\d$'
    }
}

for element in data:
    for k, v in element.items():
        if check_list[k]['format'] and \
        re.match(check_list[k]['format'], str(v)) is None:
            err_dict[k] += 1

errors = sum(v for v in err_dict.values())

print(f'Type and required field validation: {errors} error{"s"[:errors ^ 1]}')
for check in check_list:
    if check_list[check]['format']:
        print(f'{check}: {err_dict[check]}')
