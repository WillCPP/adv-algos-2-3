#
# This file compiles all the data and gives the averages of the trials
#

from pathlib import Path
files = []
data = {1: {
        0: {'x':[],'y':[]},
        1: {'x':[],'y':[]},
        2: {'x':[],'y':[]},
        3: {'x':[],'y':[]},
        4: {'x':[],'y':[]},
        5: {'x':[],'y':[]},
        6: {'x':[],'y':[]},
        7: {'x':[],'y':[]},
        8: {'x':[],'y':[]},
        9: {'x':[],'y':[]}},
    2: {
        0: {'x':[],'y':[]},
        1: {'x':[],'y':[]},
        2: {'x':[],'y':[]},
        3: {'x':[],'y':[]},
        4: {'x':[],'y':[]},
        5: {'x':[],'y':[]},
        6: {'x':[],'y':[]},
        7: {'x':[],'y':[]},
        8: {'x':[],'y':[]},
        9: {'x':[],'y':[]}},
    3: {
        0: {'x':[],'y':[]},
        1: {'x':[],'y':[]},
        2: {'x':[],'y':[]},
        3: {'x':[],'y':[]},
        4: {'x':[],'y':[]},
        5: {'x':[],'y':[]},
        6: {'x':[],'y':[]},
        7: {'x':[],'y':[]},
        8: {'x':[],'y':[]},
        9: {'x':[],'y':[]}}}
path = Path(r'/home/ubuntu/adv-algos-2-3/mp-work/')
for entry in path.iterdir():
    files.append(entry)
    s = str(entry.absolute()).split('_')
    s1 = int(s[1])
    s2 = int(s[2])
    s3 = int(s[3].split('.')[0])
    data[s1][s2]['x'].append(s3)
    with entry.open() as f: steps = int(f.readline())
    data[s1][s2]['y'].append(steps)
    data[s1][s2]['x'].sort()
    data[s1][s2]['y'].sort()
# print(data)
for k, v in data.items():
    totals = [0]*11
    for k2, v2 in v.items():
        #print(f'PROCESS {k} | TRIAL {k2+1}')
        ind = 0
        for x,y in zip(v2['x'],v2['y']):
            totals[ind] += y
            #print(f'{x}  {y}')
            ind += 1
    print(f'PROCESS {k} | AVERAGE STEPS')
    for i in range(0, len(totals)):
        print(f'{i}  {totals[i]/10}')