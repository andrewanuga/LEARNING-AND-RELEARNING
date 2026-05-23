def main():
    nums = [3,4,5,1,2]
    return check(nums)

def check(array):
    # checked for the drop_count if i > i+1 as you loop through the array 
    # then after the loop check if the end of the array is larger than
    # the beginning of it if so add to the drop_count 
    # then if the drop_count is above 1 output false else it is True 

    # The approach tries suggests that the algorithm knows what a rotated array looks like 
    arr1 = array
    length = len(arr1)
    drop_count = 0

    for idx in range(0, length - 1):
        if arr1[idx] > arr1[idx+1]:
            drop_count += 1

    if arr1[length -1] > arr1[0]: # or if arr[-1] > arr1[0]:
        drop_count += 1
    
    return drop_count <= 1


print(main())

