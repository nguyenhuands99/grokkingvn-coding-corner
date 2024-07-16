# Brute-force approach

def is_instinct(arr, i, j):
    return len(arr[i: j+ 1]) == len(set(arr[i: j+ 1]))

def longest_instinct_arr(arr):
    max_len = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_instinct(arr, i, j):
                max_len = max(max_len, j - i + 1)
    return max_len

given_arr = [5, 1, 3, 5, 2, 3, 4, 1]

print(longest_instinct_arr(given_arr)) # 5 -> O(n^2)



