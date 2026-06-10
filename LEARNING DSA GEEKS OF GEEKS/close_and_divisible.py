def main():
    m = 12
    n = 4

    closet_and_divisible_algo = closet_and_divisible2(m, n)
    print(closet_and_divisible_algo)

def closet_and_divisible(m, n):
    # Implementation for finding the closest number to m that is divisible by n
    check = 0
    while True:
        if (m - check) % n == 0:
            return m - check
        elif (m + check) % n == 0:
            return m + check
        check += 1

def closet_and_divisible2(m, n):
    lower_bound = (m // n) * n
    upper_bound = lower_bound + n

    if ((upper_bound-m) >= (m - lower_bound)):
        return lower_bound
    return upper_bound    

if __name__ == '__main__':
    main()