import json
import itertools
from collections import defaultdict


data = json.loads(input())

streets_buses = defaultdict(set)

for element in data:
    for k, v in element.items():
        if k == 'bus_id' and element['stop_name']:
            streets_buses[element['stop_name']] |= {v}
T_stop_names = [street for street in streets_buses if len(streets_buses[street]) > 1]

S_F_stop_names = set(element['stop_name'] for element in data if element['stop_type'] in ('S', 'F'))
O_stop_names = set(element['stop_name'] for element in data if element['stop_type'] == 'O')

on_demand_wrong = [street for street in O_stop_names if street in itertools.chain(S_F_stop_names, T_stop_names)]

print('On demand stops test:')
print(['OK', 'Wrong stop type:'][len(on_demand_wrong) > 0], end=' ')
print(sorted(on_demand_wrong))
