def fibonacci_number(n):
    f = [i for i in range(n+1)]
  #  print(f)

    for i in f :
        if i>=2:
            f[i]=f[i-1]+f[i-2]
 #   print(f)
    return f[n]






if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
