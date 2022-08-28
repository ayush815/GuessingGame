import random
randNumber = random.randint(1,100)
userGuess = None 
guesses = 0 
while(userGuess != randNumber):
   try:
    userGuess = int(input("Enter your guess : "))
    guesses += 1
 
    if userGuess == randNumber:
      print("You guessed it right") 
    else:
      if userGuess < randNumber:
        print("You guessed it wrong , guess it larger")
      else:
        print("You guessed it wrong , guess it smaller")
   except Exception as e:
      print(f"Your input resulted is an error, please enter only a number: {e}")
print(f"Your guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
  hiscore = int(f.read())

if (guesses<hiscore):
  print("You have just broken the hiscore")  
  with open("hiscore.txt", "w") as f:
     f.write(str(guesses))