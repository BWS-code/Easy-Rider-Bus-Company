import json
from collections import defaultdict


data = json.loads(input())
err_dict = defaultdict(int)

check_list = {
    'bus_id':       [int, 'required'],
    'stop_id':      [int, 'required'],
    'stop_name':    [str, 'required'],
    'next_stop':    [int, 'required'],
    'stop_type':    [str, '__char__'],
    'a_time':       [str, 'required']
}

for element in data:
    for k, v in element.items():
        data_type = check_list[k][0]
        required_field = check_list[k][1] == 'required'
        char_type = check_list[k][1] == '__char__'
     
        if type(v) != data_type or \
                required_field and data_type == str and not v or \
                char_type and len(v) > 1:
            err_dict[k] += 1

errors = sum(v for v in err_dict.values())

print(f'Type and required field validation: {errors} error{"s"[:errors^1]}')
for check in check_list:
    print(f'{check}: {err_dict[check]}')
