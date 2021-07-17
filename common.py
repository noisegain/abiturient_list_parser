from collections import defaultdict as dict


class Programm:
    def __init__(self, cur, cnt, ege):
        self.cur = cur
        self.cnt = cnt
        self.ege = ege


class Vuz:
    def __init__(self):
        self.programms = dict(Programm)


class Abiturient:
    def __init__(self):
        self.vuz = dict(Vuz)
        self.acc = (False, '', '', Programm(0, 0, 0))

    def add(self, vuz, prog, cur, cnt, ege=0, acc=False):
        self.vuz[vuz].programms[prog] = Programm(cur, cnt, ege)
        if acc:
            self.acc = (True, vuz, prog, Programm(cur, cnt, ege))


def get_snils(x):
    v = ''.join(c for c in x.strip() if c.isdigit())
    if len(v) != 11:
        return False
    temp = []
    for j in range(3):
        temp.append(v[j * 3:(j + 1) * 3])
    temp.append(v[-2:])
    return '-'.join(temp)
