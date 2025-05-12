# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which aaccept number from user and check whether that nummber is positive or negative or zero.
#   Input : 11      Output : Potitive number.
#   Input : -2      Output : Negative number.
#   Input :  0      Output : Zero.
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take one numbers as input from user.
#   create function as Check_number() for business logic.
#   Call the function to get the result of entered numbers.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------

def check_number(No1):
    if (No1 == 0):
        print("Zero")
    elif (No1 > 0 ):
        print("Positive Number")
    elif (No1 < 0 ):
        print("Negative Number")
    
def main():
    print("--------------------Start of the program--------------------")
    number = int(input("Enter a number"))

    check_number(number)

    print("--------------------End of the program--------------------")


if __name__ == "__main__":
    main()
