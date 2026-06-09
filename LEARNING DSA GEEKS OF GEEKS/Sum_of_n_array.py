def main():
    nums = [1, 2, 3, 4]
    my_sum_algo = Sum_of_n(nums)
    print(my_sum_algo.sum1())
    print(my_sum_algo.sum2())
    print(my_sum_algo.sum3())

class Sum_of_n:
    def __init__(self, n):
        self.n = n

    def sum1(self):
        total = 0
        for val in self.n:
            total += val
        return total

    def sum2(self):
        # recursive sum: base case empty list -> 0
        if not self.n:
            return 0
        # helper recursion on list
        def rec(arr, idx):
            if idx >= len(arr):
                return 0
            return arr[idx] + rec(arr, idx+1)
        return rec(self.n, 0)
    
    def sum3(self):
        return len(self.n) * (len(self.n) + 1) // 2

if __name__ == '__main__':
    main()