from os import path, listdir
from collections import defaultdict as dct

abit = dct(dict)
path = path.dirname(__file__)
for name in filter(lambda x: x.endswith('.csv'), listdir(path)):
    file = open(name).readlines()
    cnt = len(file)
    vuz, prog = name.removesuffix(".csv").split()
    for i, x in enumerate(file):
        v = ''.join(c for c in x.strip() if c.isdigit())
        if len(v) != 11:
            print(v)
            continue
        temp = []
        for j in range(3):
            temp.append(v[j*3:(j+1)*3])
        temp.append(v[-2:])
        s = '-'.join(temp)
        if vuz in abit[s]:
            abit[s][vuz].append(f'{i + 1}/{cnt} {prog}')
        else:
            abit[s][vuz] = [f'{i + 1}/{cnt} {prog}']

for name, x in abit.items():
    if len(x) > 2:
        print(name, x)
