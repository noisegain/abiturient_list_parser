from os import path, listdir
from common import *

abit = dict(Abiturient)
path = path.dirname(__file__)
for name in filter(lambda x: x.endswith('.csv'), listdir(path)):
    file = open(name, encoding="utf8").readlines()
    vuz, prog = file[0].strip().split(';')
    file.pop(0)
    cnt = len(file)
    for i, x in enumerate(file):
        s = get_snils(x)
        if s:
            abit[s].add(vuz, prog, i + 1, cnt)


for name, x in abit.items():
    if len(x.vuz) > 1:
        print(name)
        for n, v in x.vuz.items():
            print(' ' * 2, f'{n}:', end=' ')
            for n2, pr in v.programms.items():
                print(n2, f'{pr.cur}/{pr.cnt};', end=' ')
            print()
