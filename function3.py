def get_human_coordinates(board, current_player):
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  row = 3
  column = 3
  allowed_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
  move = input('Choose an empty field: ')

  if move.lower() == 'quit':
      print("Goodbye!") 
      quit()
  elif move.lower() not in allowed_moves:
      print('Not a valid move! Try again!')
      return get_human_coordinates(board, current_player)
  if 'a' in move.lower():
      row = 0
  elif 'b' in move.lower():
      row = 1
  elif 'c' in move.lower():
      row = 2
  if '1' in move.lower():
      column = 0
  elif '2' in move.lower():
      column = 1
  elif '3' in move.lower():
      column = 2
  if board[row][column] != ".":
      print('Place already taken! Try again!')
      return get_human_coordinates(board, current_player)
  return (row, column)

  pass


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones