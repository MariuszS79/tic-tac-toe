import random
import os

#positions on the board
positions=["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#X or O to chose
marker=["X", "O", "x", "o"]

#board for the game to place markers on 
board_numbers="_ _ _ _ _ _ _\n|   |   |   |\n|_7_|_8_|_9_|\n|   |   |   |\n|_4_|_5_|_6_|\n|   |   |   |\n|_1_|_2_|_3_|"



print(board_numbers)
print("\nHello. Welcome to tick tack toe game.\nNumbers on above board are positions. When asked for position, type in number from the board. Each position can be picked only once.\n")

player_marker=""
#player choses to use X or O
def XO():
  global marker
  global player_marker
  player_marker=input("Pick your marker: X or O: ")

#if wrong marker was typed in
  while player_marker not in marker:
    player_marker=input("Pick your marker: X or O: ")

#player's choice if plays with X
def player_X():
  global board_numbers
  global count
  player=input('\nPlace your marker "X" on the board: ')
  if player in board_numbers and player in positions:
    board_numbers=(board_numbers.replace(player, "X"))
  elif player not in board_numbers or player not in positions:
    while player not in board_numbers or player not in positions:
      player=input("type in proper number: ")
    board_numbers=(board_numbers.replace(player, "X"))
  count=count+1
  print(board_numbers)
  
#player's choice if plays with O
def player_O():
  global board_numbers
  global count
  player=input('\nPlace your marker "O" on the board: ')
  if player in board_numbers and player in positions:
    board_numbers=(board_numbers.replace(player, "O"))
  elif player not in board_numbers or player not in positions:
    while player not in board_numbers or player not in positions:
      player=input("type in proper number: ")
    board_numbers=(board_numbers.replace(player, "O"))
  count=count+1
  print(board_numbers)

corners=[board_numbers[30], board_numbers[38], board_numbers[86], board_numbers[94]]

#computer's move if plays with X
def computer_X():
  global board_numbers
  global count
  global corners
  computer=random.choice(positions)
  corner=random.choice(corners)
  
  #2 are in a row so ad 3rd
  if board_numbers[30]=="X" and board_numbers[34]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif board_numbers[38]=="X" and board_numbers[34]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif board_numbers[30]=="X" and board_numbers[38]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif board_numbers[58]=="X" and board_numbers[62]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif board_numbers[62]=="X" and board_numbers[66]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif board_numbers[58]=="X" and board_numbers[66]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif board_numbers[86]=="X" and board_numbers[90]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif board_numbers[90]=="X" and board_numbers[94]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif board_numbers[86]=="X" and board_numbers[94]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif board_numbers[30]=="X" and board_numbers[62]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif board_numbers[30]=="X" and board_numbers[94]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif board_numbers[62]=="X" and board_numbers[94]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif board_numbers[38]=="X" and board_numbers[62]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif board_numbers[86]=="X" and board_numbers[38]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif board_numbers[86]=="X" and board_numbers[62]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif board_numbers[30]=="X" and board_numbers[58]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif board_numbers[58]=="X" and board_numbers[86]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif board_numbers[30]=="X" and board_numbers[86]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif board_numbers[34]=="X" and board_numbers[62]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif board_numbers[62]=="X" and board_numbers[90]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif board_numbers[34]=="X" and board_numbers[90]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif board_numbers[38]=="X" and board_numbers[66]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif board_numbers[38]=="X" and board_numbers[94]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif board_numbers[66]=="X" and board_numbers[94]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  
  #move 1
  if count==0:
    board_numbers=(board_numbers.replace(corner, "X"))
  #------------here something keeps picking same corner twice sometimes, to be fixed
  #move 2
  elif count==2 and "5" not in board_numbers:
 
    while corner=="X" or corner=="O":
      corner=random.choice(corners)
    if corner=="1" or corner=="3" or corner=="7" or corner=="9":
      board_numbers=(board_numbers.replace(corner, "X"))
    
  
  #move 3
  elif count==4 and board_numbers[62]=="O" and board_numbers[34]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[90]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[66]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[58]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[34]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==4 and board_numbers[38]=="O" and board_numbers[34]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==4 and board_numbers[86]=="O" and board_numbers[90]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==4 and board_numbers[90]=="O" and board_numbers[94]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[58]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==4 and board_numbers[58]=="O" and board_numbers[86]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==4 and board_numbers[38]=="O" and board_numbers[66]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==4 and board_numbers[66]=="O" and board_numbers[94]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[62]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[94]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[38]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==4 and board_numbers[62]=="O" and board_numbers[86]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[38]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif count==4 and board_numbers[58]=="O" and board_numbers[66]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==4 and board_numbers[86]=="O" and board_numbers[94]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[86]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif count==4 and board_numbers[34]=="O" and board_numbers[90]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==4 and board_numbers[38]=="O" and board_numbers[94]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif count==4 and board_numbers[38]=="O" and board_numbers[86]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==4 and board_numbers[30]=="O" and board_numbers[94]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==4 and board_numbers[62]=="O":
    board_numbers=(board_numbers.replace("9", "X"))
  
#move 4
  elif count==6 and board_numbers[62]=="O" and board_numbers[34]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[90]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[66]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[58]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[34]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==6 and board_numbers[38]=="O" and board_numbers[34]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==6 and board_numbers[86]=="O" and board_numbers[90]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==6 and board_numbers[90]=="O" and board_numbers[94]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[58]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==6 and board_numbers[58]=="O" and board_numbers[86]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==6 and board_numbers[38]=="O" and board_numbers[66]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==6 and board_numbers[66]=="O" and board_numbers[94]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[62]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[94]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[38]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "X"))
  elif count==6 and board_numbers[62]=="O" and board_numbers[86]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[38]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "X"))
  elif count==6 and board_numbers[58]=="O" and board_numbers[66]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==6 and board_numbers[86]=="O" and board_numbers[94]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[86]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "X"))
  elif count==6 and board_numbers[34]=="O" and board_numbers[90]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==6 and board_numbers[38]=="O" and board_numbers[94]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "X"))
  elif count==6 and board_numbers[38]=="O" and board_numbers[86]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))
  elif count==6 and board_numbers[30]=="O" and board_numbers[94]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "X"))

  else:
    computer=random.choice(positions)
    if computer in board_numbers:
      board_numbers=(board_numbers.replace(computer, "X"))
    elif computer not in board_numbers:
      while computer not in board_numbers:
        computer=random.choice(positions)
      board_numbers=(board_numbers.replace(computer, "X"))
  count=count+1
  print(board_numbers)
  
#computer's move if plays with O
def computer_O():
  global board_numbers
  global count
  computer=random.choice(positions)
  corner=random.choice(corners)
  
  #2 are in a row so ad 3rd
  if board_numbers[30]=="O" and board_numbers[34]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif board_numbers[38]=="O" and board_numbers[34]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif board_numbers[30]=="O" and board_numbers[38]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif board_numbers[58]=="O" and board_numbers[62]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif board_numbers[62]=="O" and board_numbers[66]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif board_numbers[58]=="O" and board_numbers[66]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif board_numbers[86]=="O" and board_numbers[90]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif board_numbers[90]=="O" and board_numbers[94]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif board_numbers[86]=="O" and board_numbers[94]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif board_numbers[30]=="O" and board_numbers[62]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif board_numbers[30]=="O" and board_numbers[94]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif board_numbers[62]=="O" and board_numbers[94]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif board_numbers[38]=="O" and board_numbers[62]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif board_numbers[86]=="O" and board_numbers[38]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif board_numbers[86]=="O" and board_numbers[62]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif board_numbers[30]=="O" and board_numbers[58]=="O" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif board_numbers[58]=="O" and board_numbers[86]=="O" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif board_numbers[30]=="O" and board_numbers[86]=="O" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif board_numbers[34]=="O" and board_numbers[62]=="O" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif board_numbers[62]=="O" and board_numbers[90]=="O" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif board_numbers[34]=="O" and board_numbers[90]=="O" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif board_numbers[38]=="O" and board_numbers[66]=="O" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif board_numbers[38]=="O" and board_numbers[94]=="O" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif board_numbers[66]=="O" and board_numbers[94]=="O" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))

  #move 1
  elif count==1 and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==1 and "5" not in board_numbers:
    board_numbers=(board_numbers.replace(corner, "O"))
  
  #move 2
  elif count==3 and board_numbers[62]=="X" and board_numbers[34]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[90]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[66]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[58]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[34]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==3 and board_numbers[38]=="X" and board_numbers[34]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==3 and board_numbers[86]=="X" and board_numbers[90]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==3 and board_numbers[90]=="X" and board_numbers[94]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[58]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==3 and board_numbers[58]=="X" and board_numbers[86]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==3 and board_numbers[38]=="X" and board_numbers[66]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==3 and board_numbers[66]=="X" and board_numbers[94]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[62]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[94]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[38]=="X" and "1" in board_numbers[86]:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==3 and board_numbers[62]=="X" and board_numbers[86]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[38]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif count==3 and board_numbers[58]=="X" and board_numbers[66]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==3 and board_numbers[86]=="X" and board_numbers[94]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[86]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif count==3 and board_numbers[34]=="X" and board_numbers[90]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==3 and board_numbers[38]=="X" and board_numbers[94]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif count==3 and board_numbers[38]=="X" and board_numbers[86]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==3 and board_numbers[30]=="X" and board_numbers[94]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==3 and board_numbers[62]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))

  #move 3
  elif count==5 and board_numbers[62]=="X" and board_numbers[34]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[90]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[66]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[58]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[34]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==5 and board_numbers[38]=="X" and board_numbers[34]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==5 and board_numbers[86]=="X" and board_numbers[90]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==5 and board_numbers[90]=="X" and board_numbers[94]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[58]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==5 and board_numbers[58]=="X" and board_numbers[86]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==5 and board_numbers[38]=="X" and board_numbers[66]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==5 and board_numbers[66]=="X" and board_numbers[94]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[62]=="X" and "3" in board_numbers:
    board_numbers=(board_numbers.replace("3", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[94]=="X" and "7" in board_numbers:
    board_numbers=(board_numbers.replace("7", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[38]=="X" and "1" in board_numbers:
    board_numbers=(board_numbers.replace("1", "O"))
  elif count==5 and board_numbers[62]=="X" and board_numbers[86]=="X" and "9" in board_numbers:
    board_numbers=(board_numbers.replace("9", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[38]=="X" and "8" in board_numbers:
    board_numbers=(board_numbers.replace("8", "O"))
  elif count==5 and board_numbers[58]=="X" and board_numbers[66]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==5 and board_numbers[86]=="X" and board_numbers[94]=="X" and "2" in board_numbers:
    board_numbers=(board_numbers.replace("2", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[86]=="X" and "4" in board_numbers:
    board_numbers=(board_numbers.replace("4", "O"))
  elif count==5 and board_numbers[34]=="X" and board_numbers[90]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==5 and board_numbers[38]=="X" and board_numbers[94]=="X" and "6" in board_numbers:
    board_numbers=(board_numbers.replace("6", "O"))
  elif count==5 and board_numbers[38]=="X" and board_numbers[86]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==5 and board_numbers[30]=="X" and board_numbers[94]=="X" and "5" in board_numbers:
    board_numbers=(board_numbers.replace("5", "O"))
  elif count==5 and board_numbers[62]=="X":
    board_numbers=(board_numbers.replace("9", "O"))

  else:
    if computer in board_numbers:
      board_numbers=(board_numbers.replace(computer, "O"))
    elif computer not in board_numbers:
      while computer not in board_numbers:
        computer=random.choice(positions)
      board_numbers=(board_numbers.replace(computer, "O"))
  count=count+1
  print(board_numbers)
  
#checking for draw after 9 moves
count=0
def draw():
  global game
  global count
  if count==9 and game==True:
    os.system('clear')
    print(board_numbers)
    print ("It's a draw")
    game=False
    

# check for index of positions in board
"""
chars = []
for line in board_numbers:
   for c in line:
       chars.append(c)
print (chars)
print(chars.index("9"))
"""

#location for positions on board:
#7: board_numbers(30)
#8: board_numbers(34)
#9: board_numbers(38)
#4: board_numbers(58)
#5: board_numbers(62)
#6: board_numbers(66)
#1: board_numbers(86)
#2: board_numbers(90)
#3: board_numbers(94)

#check if X wins
def win_x():
  global game
  global board_numbers
  if board_numbers[30]=="X" and board_numbers[62]=="X" and board_numbers[94]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[30]=="X" and board_numbers[34]=="X" and board_numbers[38]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[58]=="X" and board_numbers[62]=="X" and board_numbers[66]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[86]=="X" and board_numbers[90]=="X" and board_numbers[94]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[38]=="X" and board_numbers[62]=="X" and board_numbers[86]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[30]=="X" and board_numbers[58]=="X" and board_numbers[86]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[34]=="X" and board_numbers[62]=="X" and board_numbers[90]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  elif board_numbers[38]=="X" and board_numbers[66]=="X" and board_numbers[94]=="X":
    os.system('clear')
    print(board_numbers)
    print("X wins")
    game=False
  else:
    pass

#check if O wins
def win_o():
  global game
  global board_numbers
  if board_numbers[30]=="O" and board_numbers[62]=="O" and board_numbers[94]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[30]=="O" and board_numbers[34]=="O" and board_numbers[38]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[58]=="O" and board_numbers[62]=="O" and board_numbers[66]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[86]=="O" and board_numbers[90]=="O" and board_numbers[94]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[38]=="O" and board_numbers[62]=="O" and board_numbers[86]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[30]=="O" and board_numbers[58]=="O" and board_numbers[86]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[34]=="O" and board_numbers[62]=="O" and board_numbers[90]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  elif board_numbers[38]=="O" and board_numbers[66]=="O" and board_numbers[94]=="O":
    os.system('clear')
    print(board_numbers)
    print("O wins")
    game=False
  else:
    pass

#check if player wants to play again   

def play_again():
  global game
  global loop
  again=input("Would you like to play again? y/n: ")
  if again=="y" or again=="Y":
    game=True
  else: 
    print("Have a nice day ;-)")
    loop=False

loop=True
game=True
while loop:
  XO()
  count=0
  board_numbers="_ _ _ _ _ _ _\n|   |   |   |\n|_7_|_8_|_9_|\n|   |   |   |\n|_4_|_5_|_6_|\n|   |   |   |\n|_1_|_2_|_3_|"
  while game:
    os.system('clear')
    print(board_numbers)
    for i in range(5):
      if player_marker=="X" or player_marker=="x":
        player_X()
        os.system('clear')
        win_x()
        if game==False:
          break
        draw()
        if count==9:
          break
        computer_O()
        win_o()
        if game==False:
          break
        draw()
        if count==9:
          break
        

      elif player_marker=="O" or player_marker=="o":
        os.system('clear')
        computer_X()
        win_x()
        if game==False:
          break
        draw()
        if count==9:
          break
        player_O()
        win_o()
        if game==False:
          break
        draw()
        if count==9:
          break

  play_again()
  continue

   
      
