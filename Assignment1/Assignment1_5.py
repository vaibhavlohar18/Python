# --------------------------------------------------------------------------------------------------------
#   Problem Statement :
#   Write a program which display 10 to 1  on screen. 
#   10 9 8 7 6 5 4 3 2 1 
# --------------------------------------------------------------------------------------------------------
#   Algorithm :
#   Start
#   Take for loop using rang.
#   give the range parameters e.g (Start, Stop , step) 
#   print i value on console 
#   End
# --------------------------------------------------------------------------------------------------------

def main():
    for i in range(10,0,-1) :
        print(i,end = " ")


if __name__ == "__main__":
    main()
