import random
number = random.randint(1,10)
i = [1,2,3,4,5,6,7,8,9,10]
print(i)
for r in range(9):
   try :
           inp = int(input("what number do you want to remove: "))
           if inp != number:
            print("you are doing good countino")
            n = i.remove(inp)
            print(i)
           else :
            print("you lost try again")
            break
   except:
    print("invalid input. try again")
if inp != number: 
 print("you have won")
 print(f"the number was {number} you servived")
