def most_common(nums):
    count = {} 
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    max_num = None
    max_count = 0

    for num in count:
        if count[num] > max_count:
            max_num = num
            max_count = count[num]

    return max_num
print(most_common([1, 3, 1, 3, 2, 1]))
print(most_common([4, 4, 2, 2, 2, 3]))