# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which accept name from user and display length of its name
#   2Input : Marvellous     Output 10.
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take one input as string.
#   create function as display_length() for business logic.
#   Call the function to get the result of entered string to get the length.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------

def display_length(data):
    length = len(data)
    return length

def main():
    print("--------------------Start of the program--------------------")
    io_str = input("Enter a name : ")

    result = display_length(io_str)

    print("Lenght of name  : ",result)

    print("--------------------End of the program--------------------")


if __name__ == "__main__":
    main()
