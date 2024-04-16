def lcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a

        a_dash = a % b
        return gcd(b, a_dash)
    return int(gcd(a,b)*(a/gcd(a,b))*(b/gcd(a,b)))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
