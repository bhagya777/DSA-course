def gcd(a, b):
    if b==0:
        return a

    a_dash=a%b
    return gcd(b,a_dash)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))