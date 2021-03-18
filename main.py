import random

print("Welcome to my Adventure Game")
print()
print("Basically imagine that you are on a magic carpet in a fantasy world, trying to escape from talking wolves and the magic carpet only takes pixie dust to keep going.")

wolvesDistance = 20
thirstLevel = 0
milesTraveled = 0
pixieDustLevel = 100
hungerLevel = 0
waterBottlesLeft = 3
burgersLeft = 3

print("These are your options:")
print("A = Stop to Rest")
print("B = Status Check")
print("C = Eat Some Food")
print("D = Drink Some Water")
print("E = Continue Flying")

userInput = input("Choose what you want to do - A,B,C,D, or E : ")

while(True):
  #Conditions to check for userInput
  if(userInput == "A"):
    distanceTraveled = random.randint(1,5)
    milesTraveled += distanceTraveled
    print("You Swam " + distanceTraveled)

    totalSharkMiles = random.randint(1,6)
    wolvesDistance += totalSharkMiles

    pixieDustLevel -= 10
  elif(userInput == "B"):
    if()


  elif(userInput == "C"):
    print("You chose C!")
  elif(userInput == "D"):
    print("You chose D!")
  elif(userInput == "E"):
    print("You chose E!")
  else:
    print("Please Choose a Valid Option")

  #Winning Condition
  if(milesTraveled >= 50):
    print("You Win!")
    break

  #Losing Condition
  if(wolvesDistance >= 50):
    print("You Lost, the Wolves ate You.")
    break

  #Warning Condition
  if(milesTraveled - wolvesDistance <= 5):
    print("The wolves are getting dangerously close to you!")

  #Printing the options again and asking the user fro another choice
  print("These are your options:")
  print("A = Stop to Rest")
  print("B = Status Check")
  print("C = Eat Some Food")
  print("D = Drink Some Water")
  print("E = Continue Flying")
  userInput = input("Guess Again : ")

  

