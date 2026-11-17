n = int(input())
nums = list(map(int, input().split()))
requests_n = int(input())

def get_prefix_zero_array(arr):
    n = len(arr)
    prefix_arr = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_arr[i] = prefix_arr[i - 1] + (1 if arr[i - 1] == 0 else 0)
    return prefix_arr

zeros = get_prefix_zero_array(nums)
result = []

def count_zeros(zeros, left, right):
    return zeros[right] - zeros[left - 1]

for i in range (requests_n):
    current_l, current_r = map(int, input().split())
    current_sum = count_zeros(zeros, current_l, current_r)
    result.append(str(current_sum))

print(' '.join(result))