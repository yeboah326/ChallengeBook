#3n+1 Problem
m, high = input(), 0
new = list(map(lambda x: int(x),m.split(" ")))


def cycle(n):
    ls = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            ls.append(n)
            continue
        if n % 2 != 0:
            n = (3 * n) + 1
            ls.append(n)    
            continue
        if n == 1:
            ls.append(n)
    return len(ls)

for i in range (new[0], new[-1] + 1):    
    if cycle(i) > high:
        high = cycle(i)

print(new[0],new[-1],high)    


