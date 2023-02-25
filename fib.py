import time

def fibbonachi(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonachi(n-1) + fibbonachi(n-2)


start = time.time()
print(fibbonachi(10))
end = time.time() - start
print(end)

#10 uses 0.167381 secons
#20 uses 2.596817 seconds
#30 uses 448.5339 seconds