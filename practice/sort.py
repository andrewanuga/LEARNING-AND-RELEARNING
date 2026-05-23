def main():
    array = [6,1,7,5,3,6,13,10]
    sortting = Sort(array)
    
    return (sortting.bubble_sort())

class Sort:
    def __init__(self, nums):
        self.nums = nums
        
    def bubble_sort(self):
        arr = list(self.nums) # copy self.nums To prevent the mutation of the original list
        n = len(self.nums) 

        for i in range(n): # looping through the array in i times
            swapped = False # False can also be 0 in py

            # the n - i -1 = for the array - i times of loop for registaring wher is on
            # sortted instead of starting again -1 to prevent IndexError in py
            for idx in range(0, n - i - 1): # in i times of loop, loop and swap the nums
                if arr[idx] > arr[idx + 1]:
                    arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx] # swap made
                    swapped = True # Since Swap was made put as true

            if not swapped:
                break
        return arr
        
print(main())