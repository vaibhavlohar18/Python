# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which aaccept number from user and print that number of " * " on screen
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take one numbers as input from user.
#   create function as pattern() for business logic.
#   Call the function to get the result of entered numbers.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------

def pattern(No1):
    for i in range(0,No1) :
        print("*",end = " ")


def main():
    print("--------------------Start of the program--------------------")
    number = int(input("Enter a number : "))

    pattern(number)
    
    print("\n --------------------End of the program--------------------")

if __name__ == "__main__":
    main()
