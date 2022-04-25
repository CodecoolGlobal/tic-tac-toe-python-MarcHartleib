def display_board(board):
#   """
#   Should print the tic tac toe board in a format similar to
#        1   2   3
#     A   X | O | . 
#        ---+---+---
#     B   X | O | .
#        --+---+---
#     C   0 | X | . 
#        --+---+---
#   """

  row1 = ( board[0][0] + " | " + board[0][1] + " | " + board[0][2] )
  row2 = ( board[1][0] + " | " + board[1][1] + " | " + board[1][2] )
  row3 = ( board[2][0] + " | " + board[2][1] + " | " + board[2][2] )
  
    
#   print(row1)
#   print(row2)
#   print(row3)
 
  print("  1   2   3")
  print(f"A {row1}")
  print( "  --+---+--")
  print(f"B {row2}")
  print( "  --+---+--")
  print(f"C {row3}")

  # board = [".", ".", ".",
  #         ".", ".", ".",
  #         ".", ".", "."]
  
  # row1 = "A" [board[0] + " | " + board [1] + " | " + board[2]]
  # print([board[0 + " | " + ]])
  #row1 = ( board[0] + " | " + board[1] + " | " + board[2] )
  # print( "--+---+--")
  # print ( board[3] + " | " + board[4] + " | " + board[5] )
  # print( "--+---+--")
  # print ( board[6] + " | " + board[7] + " | " + board[8] )
  pass



if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ["x", ".", "."],
      ["x", ".", "."],
      [".", ".", "."]
    ]
    display_board(board)
    # should print 
    #     1   2   3
    # A   X | O | . 
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | . 
    #    --+---+---

    