# Write a program that:
  # Asks for the user’s name.
  # Asks the user to input a number between 1 and 5.
  # Outputs a personalised fortune/message (that includes the user’s name) depending on which number they picked.

name = input("What's your name? ")
number = int(input("Choose a number between 1 and 5... "))
if number == 1:
  print("Long life is in store for you, " + name)
elif number == 2:
  print("Be aware of who is around you, " + name + ", a dubious friend may be an enemy in camouflage...")
elif number == 3:
  print("All your hard work will soon pay off, " + name)
elif number == 4:
  print(name + ", be careful who you trust, salt and sugar look the same.")
elif number == 5:
  print("It may be difficult but it will be worth it in the end, " + name + ":)")
else:
  print("Sorry, no fortune is available right now!")