def sliding_window(arr, k, m):
    n = len(arr)
    length = k + 1

    current_sum = 0
    for i in range(length):
        current_sum += arr[i]

    if current_sum == m:
        return 1

    for left in range(1, n - length + 1):
        current_sum -= arr[left - 1]
        current_sum += arr[left + length - 1]
        if current_sum == m:
            return left + 1
    return 0

n, k, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(sliding_window(nums, k, m))
