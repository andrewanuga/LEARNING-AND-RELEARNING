# CS50's Introduction to Computer Science

#A simple program that greets the user by name
def greet(name):
# name = input("what is your name? ")
    name = name.strip().title() #This line removes any leading or trailing whitespace from the input and converts the first letter of each word to uppercase.
    # print("Hello, " + name) #This line prints "Hello" followed by the name entered by the user.
    # print("Hello,", name) #This line does the same thing as the previous line, but uses a comma to separate the string and the variable.
    return (f"Hello, {name}") #This line uses an f-string to format the output, which is a more modern and efficient way to include variables in strings.

Neri = greet(name = input("what is your name? "))
print(Neri) #This line prints the result of the greet function, which is the greeting message with the user's name.



def greetFullName(full_name):
    first_name, last_name = full_name.strip().title().split() #This line removes any leading or trailing whitespace from the input and converts the first letter of each word to uppercase.
    return (f"Hello, {first_name} {last_name}") #This line uses an f-string to format the output, which is a more modern and efficient way to include variables in strings.


full_name = input("what is your full name? ")
Neri = greetFullName(full_name) #This line prints the result of the greetFullName
print(Neri)