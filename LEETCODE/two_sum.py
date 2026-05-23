def two_sum(nums, target):
    # pick a number in nums
    # loop through nums checking
    # if the addition of number and
    # the character in nums is equal to the target
    # output the two that match else return an empty array
    check = {}

    for idxi,i in enumerate(nums):
        needed_number = target - i
        
        if needed_number in check:
            return [check[needed_number], idxi]
        
        check[i] = idxi
    return[]


nums = [3,2,4]
target = 6

print(two_sum(nums, target))