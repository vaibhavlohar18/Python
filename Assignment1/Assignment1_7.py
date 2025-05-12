# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which contains one function that accepts one number from user
#   and return TRUE if number is divisible by 5 otherwise return FALSE
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take one numbers as input from user.
#   create function as is_Divisible() for business logic.
#   Call the function to get the result of entered numbers.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------
def is_Divisible(No1):
    if((No1 % 5) == 0 ):
        return True
    else:
        return False


def main():
    print("--------------------Start of the program--------------------")
    number = int(input("Enter a number : "))

    result = is_Divisible(number)

    print("Number is divicible by 5 : ",result)

    print("--------------------End of the program--------------------")

if __name__ == "__main__":
    main()
