
# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which contains one function named as Add() which accepts two numbers from user 
#   and return addtion of that two numbers.
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take two numbers as input from user.
#   Store this two numbers  as NUM1 and Num2
#   create function as Add() for business logic.
#   Call the function to get the result of entered numbers.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------


def Add(Value1 , Value2):
    Sum = Value1 + Value2
    return Sum

def main():
    print("--------------------Start of the program--------------------")
    print("Enter First Number")                 #Take First input from end user
    Num1 = int(input())                         #Storing the entered value in Num1 variable

    print("Enter Second Number")                #Take Second input from end user 
    Num2 = int(input())                         #Storing the entered value in Num2 variable

    Result = Add(Num1, Num2)                    #Call the function to perform the logic.

    print("Addition = ", Result)                #print the result on console.

    print("--------------------End of the program--------------------")


if __name__ == "__main__":
    main()
