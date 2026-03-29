def tutorial():
  print("\n--- TUTORIAL ---")
  print("Controls:")
  print("w - Move forward")
  print("a - Move left")
  print("s - Move backward")
  print("d - Move right")
  print("e - Search")
  print("!help - See help")
def start_game():
  inventory = {"key": False, "gun": False, "flashlight": False}
  current_level = 6
  monster_attempts = 0

  print("You have woken up from a long slumber, in a delapidated lab of some kind. You feel like you've been hit with a frying pan")
  print("It seems to be some kind of Research Center, where they experimented on humans. You need to get out of this place.")
  print("If you need help, type in !help")

  while True:
    move = input(f"\n[{current_level}-th level] What do you want to do: ").strip().lower()

    if move == "!help":
      tutorial()
      continue
    elif not move:
      print("Invalid input. Type in !help if you need instructions.")
      continue

    #Floor 6
    if current_level == 6:
      if move == "w":
        print("You went through the floor and found a staircase. You're now entering floor 5.")
        current_level = 5
      elif move == "e":
        print("You've searched the area. You found nothing interesting.")
        continue
      else:
        print("Invalid input. Try again.")
        continue

    #floor 5
    elif current_level == 5:
      if move == "e":
        print("You found an armory room, and in that room, there's only one shotgun. And it's loaded. Sweet!")
        inventory["gun"] = True
      elif move == "w":
        print("You went through the floor and found a staircase. You're now entering floor 4.")
        current_level = 4
      elif move == "a" or "d":
        print("You found nothing but dead bodies, laying on desks and on the floor. Try again.")
        continue
      else:
        print("Invalid input. Try again.")
        continue

    #floor 4
    elif current_level == 4:
      if move == "e":
        print("You've searched the area. You found a note. Do you want to read? yes/no")
        choice = input().strip().lower()
        if choice == "yes":
          print("It says get out of here while you can. This place is not safe and never will be. Beware for...")
          print("This means you're not alone in this hellhole.")
          continue
        elif choice == "no":
          print("You ignored the note and moved on")
        else:
          print("Invalid input. Try again.")
          continue
      elif move == "w":
        print("You went through the floor and found a big drawer. You opened one of them and found a key. Nice!")
        inventory["key"] = True
        print("You're now entering floor 3. But you're starting to hear weird noises..")
        current_level = 3
      elif move == "a" or "d":
        print("You found nothing interesting. You moved on to the next floor.")
        current_level = 3
      else:
        print("Invalid input. Try again")
        continue

    #floor 3
    elif current_level == 3:
      print("The weird noises are getting louder and you further explore the floor until you find a mutated creature!")
      choice = input("Do you want to fight or run? fight/run: ").strip().lower()
      if choice == "fight":
        if inventory["gun"]:
          print("With the help of your shotgun, you managed to kill the creature. The floor is now safe.")
          print("You have now entered floor 2")
          current_level = 2
        else:
          print("You tried to fight the monster with your bare hands. You're dead.")
          break
      elif choice == "run":
        print("You ran away from the monster. But the monster is starting to catch up to you. Which way will you go?")
        direction = input("Direction: ").strip().lower()
        if direction == "a":
          print("You found the staircase to the next floor. You're now entering floor 2")
          current_level = 2
        elif direction == "d":
          print("You have reached a dead end.")
          if inventory["gun"]:
            print("With the shotgun you found before, you managed to finish the monster off. You are now entering floor 2")
            current_level = 2
          else:
            print("You tried to fight the monster with your bare hands, but it wasn't enough. You're dead.")
            break
        else:
          print("Invalid input. Try again.")
          continue
      else:
        print("Invalid input. Try again.")
        continue

    #floor 2
    elif current_level == 2:
      if move == "e":
        print("You found some sort of supply room. You enter and find shattered glasses, you think that this is where things went down.")
        continue
      elif move == "w":
        print("You found a dead end. Try to go somewhere else.")
        continue
      elif move == "a":
        print("You see an opened door and hear a woman crying. It's unsettling and you decide to go away.")
        continue
      elif move == "d":
        print("You found a staircase. You're now entering floor 1")
        current_level = 1
      else:
        print("Invalid input. Try again.")
        continue

    #floor 1
    elif current_level == 1:
      print("You found the exit, but it's locked!")
      if inventory["key"]:
        print("With the key that you found earlier, you managed to escape! YOU HAVE BEATEN THE GAME")
        break
      else:
        print("You need to find a key to open it. Maybe the key is in the basement!")
        current_level = 0

    #basement
    elif current_level == 0:
      print("It's pretty dark down there, but something feels off and you don't know why.")
      if move == "e":
        print("You found a flashlight! That will help.")
        inventory["flashlight"] = True
        choice = input("Do you want to explore the basement? yes/no: ").strip().lower()
        if choice == "yes":
          print("You have searched the area and you found a crying woman. Do you want to talk to her? yes/no: ")
          choice2 = input().strip().lower
          if choice2 == "yes":
            print("She gets agitated and starts chasing you. You tried to outrun her, but she catched up. You're dead")
            break
          elif choice2 == "no":
            print("You ignored the woman and moved on. You found no keys and you hear a door getting locked. You're trapped.")
            break
          else:
            print("Invalid input. Try again.")
            continue
        elif choice == "no":
          print("You decide not to explore the basement. But you hear something behind you. It's the monster from before.")
          break
        else:
          print("Invalid input. Try again")
      elif move == "w" or "a" or "d":
        print("You wander in the dark and you get lost. You hear a door getting locked. You're trapped.")
        break
      else:
        print("Invalid input. Try again.")
        continue

start_game()
