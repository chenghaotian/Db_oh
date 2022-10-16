# -*- coding:utf-8 -*-

def d_boh(a, b):
    print(b)
    try:
        b = int(a)
    except ValueError:
        return [False]
    else:
        print(f"Dec:{int(b)}")
        print(f"Bin:{bin(b)}")
        print(f"Oct:{oct(b)}")
        print(f"Hex:{hex(b)}")
        print(f"{hex(b)}")
        return [True]


