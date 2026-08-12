def main():
    try:
        number = int(input("Enter a Number: "))
        if type(number) != int:
            raise Exception("enter a Number")
    
        return even_or_odd(number)
    except ValueError:
        return {"error: Add a real number prefferably a Number"}

class check_number_state:
    def __init__(self, num):
        self.num = num
    def even_or_odd(self):
        if self.num % 2 == 0:
            return "Even"
        return "Odd"

    def is_even(self):
        return 1 if self.num % 2 == 0 else 0

    def is_odd(self):
        return 1 if self.num % 2 != 0 else 0



print(main())