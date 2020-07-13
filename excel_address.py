import re

def __find(address):
    return re.finditer(r'(^|,)(([a-zA-Z]+[0-9]+\:[a-zA-Z]+[0-9]+|[a-zA-Z]+[0-9]+)|[a-zA-Z]+:[a-zA-Z]|[0-9]+:[0-9]+)', address)

def get_column_letters(column_number):
    if column_number < 0:
        raise ValueError(column_number)

    letters = ''
    power = column_number
    while(power > 0):
        cn = power % 26
        power = int(power / 26)
        letters = chr(cn + 64) + letters

    return letters

def get_column_number(column_letters):
    if not re.match('[a-zA-Z]+$', column_letters):
        raise ValueError(column_letters)

    column_letters = column_letters.upper()

    column_number = 0
    for i in range(1, len(column_letters)+1):
        cn = ord(column_letters[i-1]) - 64

        if(i == len(column_letters)):
            column_number += cn
            continue

        column_number += cn * 26 ** (len(column_letters) - i)

    return int(column_number)


def get_rows_from_address(address):
    rows = []
    
    for f in __find(address):
        m = f.group(0)
        r = re.findall(r'[0-9]+', m)

        if ':' in m:
            if len(r) == 0:
                continue
            
            l = int(min(r[0], r[1]))
            h = int(max(r[0], r[1]))

            rows.extend(range(l, h+1))
        else:
            rows.append(int(r[0]))

    return rows

def get_columns_from_address(address):
    cols = []

    for f in __find(address):
        m = f.group(0)
        c = re.findall('[a-zA-Z]+', m)

        if ':' in m:
            if len(c) == 0:
                continue

            cn = (
                get_column_number(c[0]),
                get_column_number(c[1])
            )

            l = min(cn[0], cn[1])
            h = max(cn[0], cn[1])

            cols.extend(range(l, h+1))
        else:
            cn = get_column_number(c[0])
            cols.append(cn)

    return cols
