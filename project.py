
import random

def gameV(comp, plY):
    if comp==plY:
        return None
    if comp=='snake':
        if plY=='w':
            return False
        elif plY=='gun':
            return True
    if comp=='water':
        if plY=='gun':
            return False
        elif plY=='snake':
            return True
    if comp=='gun':
        if plY=='water':
            return True
        elif plY=='snake':
            return False


print("Computer turn: Snake(s), water(w) or gun(g)?? ")
raNo = random.randint(1,3)
print(raNo)
if raNo==1:
    comp = 'snake'
elif raNo==2:
    comp = 'water'
else:
    comp = 'gun'

plY = input("Your turn: Snake(s), water(w) or gun(g)??\n")

a = gameV(comp, plY)

print(f"computer chose {comp}")    # With the help of "f" we can add--> {} to our sentence
print(f"You chose {plY}")


if a== None:
    print("\nThis game is tie!!!!!!!!!!")
elif a:
    print("\nYou win!!!!!!!")
else:
    print("\nYou lose!!!!!!!!")
