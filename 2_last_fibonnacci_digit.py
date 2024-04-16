def fibonacci_last_digit(n):
    f = [i for i in range(n + 1)]
    #  print(f)

    for i in f:
        if i >= 2:
            f[i] = (f[i - 1] + f[i - 2])%10
    #   print(f)
    return f[n]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
