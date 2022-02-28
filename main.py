import json
import pprint
from collections import defaultdict


data = json.loads(input())

streets_buses = defaultdict(set)
buses_types = defaultdict(set)

for element in data:
    for k, v in element.items():
        if k == 'bus_id' and element['stop_name']:
            streets_buses[element['stop_name']] |= {v}
            buses_types[element[k]] |= {element['stop_type']}

# pprint.pprint(streets_buses, compact=True)
# pprint.pprint(buses_types, compact=True)

ids_missing_S_or_F = [k for k, v in buses_types.items() for typ in ('S', 'F') if typ not in v]

if ids_missing_S_or_F:
    print(f'There is no start or end stop for the line: {ids_missing_S_or_F[0]}.')
else:
    start_stop_names = set(element['stop_name'] for element in data if element['stop_type'] == 'S')
    finish_stop_names = set(element['stop_name'] for element in data if element['stop_type'] == 'F')
    transfer_stop_names = [street for street in streets_buses if len(streets_buses[street]) > 1]
    print(f'Start stops: {len(start_stop_names)} {sorted(list(start_stop_names))}')
    print(f'Transfer stops: {len(transfer_stop_names)} {sorted(transfer_stop_names)}')
    print(f'Finish stops: {len(finish_stop_names)} {sorted(list(finish_stop_names))}')
