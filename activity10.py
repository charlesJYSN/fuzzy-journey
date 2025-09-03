from getpass import getpass

user = 'CharlesJayson'
pword = 'hahaediwow'

u = input("Username-->")
p = getpass("Password-->")
 
if u == user and p == pword:
        print("You're amazing!")

else: 
        print("Try again bro:(")