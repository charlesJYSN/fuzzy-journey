name = input("Hi, what's your name?--->")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n\tODD SECTOR,press 0 to stop the loop\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
odd_nums = ''
even_nums = 0

while True:
    number = eval(input("enter a random number->>"))
    if number %2 == 1:
        print("ODD NUMBER\n__________________")
        continue
    else:
        print("EVEN NUMBERS\n__________________")
