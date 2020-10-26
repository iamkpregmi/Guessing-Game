#Guessing game in python
import random

print("*********************************************")
print("          WELCOME TO GUSSING GAME")
print("*********************************************")
startnum = int(input("Enter Starting Number: "))
endnum = int(input("Enter End Number: "))

while 1>0:
      #Generate rangom number
      randnum = random.randint(startnum,endnum)
      
      gussingnum = int(input("Enter Guessing Number: "))

      if randnum == gussingnum:
            print("You're Win")
      else:
            print("You're Lost")

      confirm = input("Do you want to Exit Y/N : ")
      print("*********************************************")
      if confirm == "Y" or confirm == "y":
            exit()
#Gussing game code end here
