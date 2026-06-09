def main():
    nums = 4
    my_sum_algo = Sum_of_n(nums)
    print(my_sum_algo.sum1())
    print(my_sum_algo.sum2())
    print(my_sum_algo.sum3())

class Sum_of_n:
    def __init__(self, n):
        self.n = n

    def sum1(self):
        total = 0
        for i in range(1, self.n + 1):
            total += i
        return total

    def sum2(self):
        if self.n == 1:
            return 1 
        return self.n + Sum_of_n(self.n - 1).sum2()
    
    def sum3(self):
        return self.n * (self.n + 1) // 2

if __name__ == '__main__':
    main()