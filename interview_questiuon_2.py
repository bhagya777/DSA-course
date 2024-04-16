
def sum(n,l,r):
    sum=0
#    print(n[0])
    x=len(n)
    if l<=x and r<=x:
        for i in range(l,r+1):
            sum+=n[i]
            l+=1
        return sum

if __name__ == '__main__':
    n = list(map(int,input().strip().split()))
    #    print(n)
    l,r = map(int, input().split())
    print(sum(n,l,r))
