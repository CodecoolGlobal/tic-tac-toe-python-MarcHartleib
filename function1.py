def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  print("Welcome to Tic Tac Toe\n")
  print("Please chose your game mode:")
  print("1. Human vs Human")
  print("2. Random AI vs Random AI")
  print("3. Human vs Random AI")
  print("4. Human vs Unbeatable AI\n")
  
  while True:
      gamemode = input("")
      if gamemode.isdigit():
        gamemode = int(gamemode)
        if gamemode > 4 or gamemode < 1:
          print("Invalid input, try again")
        else:
          for difficulty in range(1,5):
            if difficulty == gamemode:
              return difficulty
            else:
              difficulty += 1
      else:
        print("Invalid input, try again")


  pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1