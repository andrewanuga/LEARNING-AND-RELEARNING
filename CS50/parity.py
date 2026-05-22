def main(x):
    print("Even" if is_even(x) else "Odd")


def is_even(n):
    return n % 2 == 0
    # return True if n % 2 == 0 else False

main(10)