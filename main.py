import json


data = json.loads(input())
time_catches = dict()

last_time = ''
last_id = data[0]['bus_id']

for bus_id in {element['bus_id'] for element in data}:
    for element in data:
        if element['bus_id'] == bus_id and type(element['a_time']) == str and \
                    element['a_time'] and element['stop_name']:
            current_time, current_id = element['a_time'], element['bus_id']
            if current_id != last_id:
                last_time = ''
            if current_time < last_time:
                time_catches[element['bus_id']] = element['stop_name']
                break
            last_time, last_id = current_time, current_id

print('\n'.join(('Arrival time test:', *[f'bus_id line {k}: wrong time on station {v}'
                                         for k, v in time_catches.items()])) if time_catches else 'OK')
