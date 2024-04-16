

def pisanoPeriod():
    previous, current,sum = 0, 1,0
    f=[0]
    for i in range(0, 10*10):
        sum+=current
        f.append(sum%10)
        previous, current = current, (previous + current) % 10
        if (previous == 0 and current == 1):
            return i + 1,sum%10,f

def fib(m,n):
    p,s,f = pisanoPeriod()
#    print(p,s,f)
    n = n % p
    if m==0:
        return s+f[n]
    else:
        m_dash=(m-1)%p
        sumn= s+f[n]
        summ=s+f[m_dash]
#        print(summ,sumn)
        if (summ<=sumn):
            return sumn-summ
        else:
            sn_dash=sumn+10
            return sn_dash-summ



if __name__ == '__main__':
    m,n = map(int, input().split())
    print(fib(m,n))
