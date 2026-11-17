def build_prefix(arr):
    n, m = len(arr), len(arr[0])
    prefix_arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            prefix_arr[i][j] = arr[i][j]
            if i > 0:
                prefix_arr[i][j] += prefix_arr[i-1][j]
            if j > 0:
                prefix_arr[i][j] += prefix_arr[i][j-1]
            if i > 0 and j > 0:
                prefix_arr[i][j] -= prefix_arr[i-1][j-1]

    return prefix_arr

def query(prefix_arr, x1, x2, y1, y2):
    result = prefix_arr[x2][y2]
    if x1 > 0:
        result -= prefix_arr[x1-1][y2]
    if y1 > 0:
        result -= prefix_arr[x2][y1-1]
    if x1 > 0 and y1 >0:
        result += prefix_arr[x1-1][y1-1]
    return result

n, m, q = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

prefix = build_prefix(matrix)
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(query(prefix, x1 - 1, x2 - 1, y1 - 1, y2 - 1))
