name = input("What's your name? ").strip().capitalize()

match name:
    case "Harry" | "Hermione" | "Ron":
        print(f"{name} is in Gryffindor")
    case "Draco":
        print(f"{name} is in Slytherin")
    case _:
        print(f"{name} not yet registered")