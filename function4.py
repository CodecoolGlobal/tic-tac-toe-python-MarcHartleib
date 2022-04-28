import random
from function7 import is_board_full

def get_random_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  row = 3
  column = 3
  allowed_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
  ai_move = random.choice(allowed_moves)

  # elif ai_move not in allowed_moves:
  #     print('Not a valid ai_move! Try again!')
  #     return get_human_coordinates(board, current_player)
  while is_board_full(board) == False:


    if 'a' in ai_move:
        row = 0
    elif 'b' in ai_move:
        row = 1
    elif 'c' in ai_move:
        row = 2
    if '1' in ai_move:
        column = 0
    elif '2' in ai_move:
        column = 1
    elif '3' in ai_move:
        column = 2
    if board[row][column] != ".":
      return get_random_ai_coordinates(board, current_player)
    return (row, column)

  
  # for subboard in board:
  #   if "." in subboard:
  #     x = (board.index(subboard), subboard.index("."))
  #     return x
    
  
  # free_cor = [(i1, i2) for (i1, v1) in enumerate(board) for (i2, v2) in enumerate(v1) if v2 == "."]
  # return free_cor


   


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["O", "O", "."],
    [".", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)

  board_2 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print(get_random_ai_coordinates(board_2, "O")) # the printed coordinate should be None