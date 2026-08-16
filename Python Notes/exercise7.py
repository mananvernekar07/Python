#Guess the Lucky number
import random
print("To guess the lucky number type 'play'")
userplay = input()
if userplay == "play":
   def play_game():
    lucky_num = random.randint(1,50)

    while True:
       guess = int(input("Guess the lucky number:"))

       if guess == lucky_num:
           print(f"{lucky_num}! U WON!!!🎉")
           break

       elif lucky_num-5 <= guess < lucky_num:
           print("Guess is little low👀!")

       elif lucky_num < guess <= lucky_num+5:
           print("Guess is little high👀!")
           
       elif guess <= lucky_num:
           print("Guess is too low!")

       elif guess >= lucky_num:
           print("Guess is too high!")

play_game() 
        