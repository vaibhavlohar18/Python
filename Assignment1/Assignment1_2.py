# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which contains one function named as ChkNum() which accept one parameter as number.
#   If number is even then it should display "Even number" otherwise display "Odd number" on console.
#   Input: 11           Output : Odd Nummber
#   Input: 8            Output : Even Number
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Take one input from user.
#   create function as ChkNum for business logic.
#   Display the result on console.
# --------------------------------------------------------------------------------------------------------


def ChkNum(in_number):
    result = in_number % 2 
    if in_number == 0:
        print("Number Is ",in_number)
    elif result == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("-------------------------------------------------")
    print("Enter a Number :")

    number1 = int(input())
    ChkNum(number1)
    print("-------------------------------------------------")

if __name__ == "__main__":
    main()
