anime = []
title = True

while title == True:
    name = input("Enter anime title (type 'exit' to Stop)-->").lower()
    if name == "exit":
        print("\nYour list of anime you typed:")
        break

    anime.append(name)
    print(f"{name} has been added to your anime list.")

for i in anime:
    print(f"- {i}")