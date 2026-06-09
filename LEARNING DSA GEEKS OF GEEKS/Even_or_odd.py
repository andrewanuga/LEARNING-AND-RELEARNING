def main():
    try:
        number = int(input("Enter a Number: "))
        if type(number) != int:
            raise Exception("enter a Number")
    
        return even_or_odd(number)
    except ValueError:
        return {"error: Add a real number prefferably a Number"}


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(main())