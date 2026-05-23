def sort_it(nums):
    arr = list(nums) # copy nums To prevent the mutation of the original list
    n = len(nums) 

    for i in range(n): # looping through the array in i times
        swapped = False # False can also be 0 in py

        # the arr - i -1 = for the array - i times of loop for registaring wher is on
        # sortted instead of starting again -1 to prevent IndexError in py
        for idx in range(0, arr - i - 1): # in i times of loop, loop and swap the nums
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx] # swap made
                swapped = True # Since Swap was made put as true

        if not swapped:
            break
    return arr
        