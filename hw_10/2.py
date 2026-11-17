def get_prefix_sum(arr):
    prefix_arr = [0]
    current_sum = 0

    for i in arr:
        current_sum += i
        prefix_arr.append(current_sum)
    return prefix_arr

def get_interval_sum(arr, left, right):
    return arr[right + 1] - arr[left]


def get_maximal_sum(arr):
    prefix_arr = get_prefix_sum(arr)
    start, end, max_sum = 1, 1, arr[0]
    n = len(prefix_arr)

    min_value_index = 0
    min_value = prefix_arr[0]

    for i in range(1, n, 1):
        current_r = i
        current_sum = get_interval_sum(prefix_arr, min_value_index, current_r - 1)

        if (current_sum > max_sum):
            start, end, max_sum = min_value_index + 1, current_r, current_sum

        if prefix_arr[i] < min_value:
            min_value = prefix_arr[i]
            min_value_index = i
        
        
    print(start, end, max_sum)


        
n = int(input())
nums = list(map(int, input().split()))

get_maximal_sum(nums)
