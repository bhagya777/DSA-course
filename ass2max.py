def max_pairwise_product(numbers):
    sorted_list=sorted(numbers,reverse=True)
    max_product=sorted_list[0]*sorted_list[1]
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
