def pisanoPeriod():
    previous, current,sum = 0, 1,0
    f=[0]
    for i in range(0, 10*10):
        sum+=current*current
        f.append(sum%10)
        previous, current = current, (previous + current) % 10
        if (previous == 0 and current == 1):
            return i + 1,sum%10,f

def fib(n):
    p,s,f = pisanoPeriod()
#    print(p,s,f)
    n = n % p
    return s+f[n]


if __name__ == '__main__':
    n = int(input())
    print(fib(n))