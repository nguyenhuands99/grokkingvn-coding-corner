''' Grokking Newsletter #172
Given a array of non-negative numbers, your position is at the beginning, at which you start to jumpt to next position. Every elements indicate the maximum jump for you to jump. E.g if the first element is 2, then you can jump 1 or 2 to the next position. Now, determine whether you can jump to the last index of the array.

E.g1:
    input: nums = [2,3,1,1,4]
    output: true
    Explain: idx 0: jump 1, idx 1: jump 3 to the last idx(4).

E.g 2:
    input nums = [3,2,1,0,4]
    output: false
    Explain: No matter what, you will end up at idx 3, which is 0 and you cannot jump anymore.
'''

# input: array[N], N? maximum? 
# output: true/ false
# approach: iterate backwards from the next-to-last idx, if their value + their idx >= len -> we can jump the last idx from them, green flag. Now what? idx 
# 
nums = [3,2,1,0,4]

def jump_to_end(nums):
    endpoint = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] + i >= endpoint:
            endpoint = i
    return endpoint == 0

print(jump_to_end(nums))

