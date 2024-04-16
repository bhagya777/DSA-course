
f=[0,1]
def fibonacci_number(n):
    if n<len(f):
        return f[n]
    else:
        f.append(fibonacci_number(n-1)+fibonacci_number(n-2))
        return f[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
