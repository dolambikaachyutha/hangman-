import random
import time
from colorama import Fore,Style
print(Fore.BLUE+Style.BRIGHT+"Welcome to hangman game")
time.sleep(1)
print(Style.BRIGHT + "        RULES OF THE GAME      ")
time.sleep(1)
print("Note computer will choose a random word from the category you choose")
time.sleep(1)
print("You have 6 lives to guess the word")
time.sleep(1)
print("Note: You can guess only one letter at a time")
time.sleep(1)
print("Note: If your guess is wrong you will loss one live")
time.sleep(1)
print("Note: If you lose all the lives you will lose the game")
time.sleep(1)
print("Note: If you guess the word correctly you will win the game")
time.sleep(1)
print("Note: make sure to choose lowercase letters only")
time.sleep(1)
print("Lets start the game")
movies=["avatar","hinanna","avengers","jersey","hello","godavari","msdhoni","lovestory"]
animals=["elephant","hippo","rhinoceros","gorilla","monkey","crocodile","tortoise","cheetah"]
foods = ["dosa","idli","vada","uttapam","sambar","rasam","upma","appam","payasam","biryani"]
options=["movies","animals","foods"]
names=["kedaar","supriya","dolambika","chandra","sowmya","gayathri","kavya","karthikeya","srikanth"]
choices=input("Choose one of the following categories: movies,animals,foods,names\n")
if choices=="movies":
  hidden_word=random.choice(movies)
elif choices=="animals":
  hidden_word=random.choice(animals)
elif choices=="foods":
  hidden_word=random.choice(foods)
elif choices=="names":
  hidden_word=random.choice(names)
else:
  print("Invalid Choice,please choose one of the following categories: movies,animals,foods,names")   
  exit()   
word=[]
for letter in range(len(hidden_word)):
  word.append("_")
hangman = [

"""
 O
""",

"""
 O
 |
""",

"""
 O
/|
""",

"""
 O
/|\\
""",

"""
 O
/|\\
/
""",

"""
 O
/|\\
/ \\
"""
]
lives=6
game=False
guessed_letters=[]
while not game:
 print(" ".join(word))
 print("Guessed letters:"," ".join(guessed_letters))
 guess=input("enter you guess\n")
 guessed_letters.append(guess)
 if len(guess) != 1:
  print("Enter only one letter")
  continue
 for letter in range(len(hidden_word)):
      if hidden_word[letter]==guess:
        word[letter]=guess
 if guess not in hidden_word:
          lives -= 1
          print("You lossed one life")
          print(Fore.RED+Style.BRIGHT+"Wrong Guess")
          time.sleep(1)
          print(hangman[6-lives-1])
          time.sleep(1)
          print("Remaining Lives:", lives)
 if lives==0:
  print(Fore.RED +Style.BRIGHT + "Wrong Guess")  
  time.sleep(1)
  print("The word was:",hidden_word)
  game=True
 if "_" not in word:
  print(Fore.GREEN +Style.BRIGHT + "Correct Guess")
  game=True 
