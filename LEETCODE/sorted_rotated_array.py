def main():
    nums = [3,4,5,1,2]
    return check(nums)

def check(array):
    arr1 = array
    length = len(arr1)
    drop_count = 0

    for idx in range(0, length - 1):
        if arr1[idx] > arr1[idx+1]:
            drop_count += 1

    if arr1[length -1] > arr1[0]:
        drop_count += 1
    
    return drop_count <= 1


print(main())