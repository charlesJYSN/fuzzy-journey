wash= True
while wash == True:
    wash_again = input("DO YOU WANT TO WASH AGAIN?yes/no?").lower()
    yes = wash
    if wash == yes:
        print("WASHED ")
    else:
     print("Okay, DONE WASHING")
    break