# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which display first 10 even numbers on the screen.
#   2   4   6   8   10  14  16  18  20
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   create function as display_even_no() for business logic.
#   Call the function to get the result of entered numbers.
#   Display the result on console.
#   END.
# --------------------------------------------------------------------------------------------------------
def display_even_no():
    for i in range(1,11):
        print(i * 2, end = " ")
        
    

def main():
    print("--------------------Start of the program--------------------")

    display_even_no()

    print("\n --------------------End of the program--------------------")

if __name__ == "__main__":
    main()
