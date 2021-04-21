from cs50 import get_string

cn = get_string("Number: ")

rev_cn = cn[:: -1]
Luhns = sum([(int(n)*2)//10 + ((int(n) * 2) % 10) for n in rev_cn[1::2]]) + sum([int(x) for x in rev_cn[::2]])


if Luhns % 10 == 0:
    if len(cn) == 15 and cn[0:2] in ['34', '37']:
        print("AMEX")
    elif len(cn) == 16 and 51 <= int(cn[0:2]) <= 55:
        print("MASTERCARD")
    elif len(cn) in [16, 13] and cn[0] == '4':
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
    