name = input("What's your name?")
amount = eval(input("How much is your fare?"))
quantity = eval(input("How many?"))

y= 'yes'
ys = input("Are you a student?")
total_cost = amount * quantity
if total_cost >=100:
            print("Okay, you have a discount of 20%")
            total = total_cost * .20
            total_price = total - total_cost
            print("Your total will be", total_price)
else: 
        print("sorry man you don't have a discount")