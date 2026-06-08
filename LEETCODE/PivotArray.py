# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.

def main():
    nums = [9,12,5,10,14,3,10] # [-3,4,3,2]
    pivot = 10 # 2
    return pivotArray(nums, pivot)

def pivotArray(nums, pivot):
    length = len(nums)
    smaller_list=[]
    larger_list=[]
    equal_list=[]

    for i in range(length):
        if nums[i] < pivot:
            smaller_list.append(nums[i])
        elif nums[i] > pivot:
            larger_list.append(nums[i])
        else:
            equal_list.append(nums[i])

    added_list = smaller_list + equal_list + larger_list
    return(added_list)

print(main())