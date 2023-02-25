def atoi(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    elif s[0] in list('abcdefghijklmnopqrstuvwxyz'):
        return 0
    elif s[0] in list('abcdefghijklmnopqrstuvwxyz'):
        return 0
    s = s.split(".")[0].strip()
    k = ""
    stop = False
    for i in s:
        if i == "+" and k != "":
            stop = True
            break
        elif i == "-" and k != "":
            stop = True
            break
        for x in list('abcdefghijklmnopqrstuvwxyz '):
            if i == x and x != " ":
                k = clean(k, i)
                stop = True
                break
            elif i == x and k != "":
                stop = True
                break
            else:
                continue
        if stop:
            break
        k = k + i
    if k == "":
        return 0
    if k[0] == "-":
        k = k[1:]
        k = k.replace("-", "")
        if "+" in k:
            return 0
        for i in k:
            if i == "0":
                k = k[1:]
            else:
                break
        if k == "":
            return 0
        if k.replace("+", "").isnumeric():
            if int(k)*-1 > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif int(k)*-1 < -2 ** 31:
                return -2 ** 31
            return int(k)*-1
        else:
            return 0
    else:
        k = k.replace("+", "")
        for i in k:
            if i == "0":
                k = k[1:]
            else:
                break
        if k == "":
            return 0
        if k[0].isnumeric():
            if int(k) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif int(k) < -2 ** 31:
                return -2 ** 31
            return int(k)
        else:
            return 0

def clean(s, i):
    if i in list('abcdefghijklmnopqrstuvwxyz '):
        return s.replace(i, "")
    else:
        return s

if __name__ == "__main__":
    print(atoi("+8+4"))