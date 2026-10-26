
def inputLogic():
    
    enteredCharacters = []

    while True:
        Userinput = input()
        if Userinput == "=":
            break
        else:    
            enteredCharacters.append(Userinput)

            for char in enteredCharacters:
                print(char, end="")

    print("Final Result: ")
    for char in enteredCharacters:
                    print(char, end="")

    print(f" = {eval("".join(enteredCharacters))}")