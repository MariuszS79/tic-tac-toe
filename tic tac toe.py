import random
import os

positions=["1", "2", "3", "4", "5", "6", "7", "8", "9"]

marker=["X", "O", "x", "o"]

board_numbers="_ _ _ _ _ _ _\n|   |   |   |\n|_7_|_8_|_9_|\n|   |   |   |\n|_4_|_5_|_6_|\n|   |   |   |\n|_1_|_2_|_3_|"

board=list(board_numbers.split(" "))

print(board_numbers)
print("\nHello. Welcome to tick tack toe game.\nNumbers on above board are positions. When asked for position, type in number from the board. Each position can be picked only once.\n")

player_marker=input("Pick your marker: X or O: ")
while player_marker not in marker:
  player_marker=input("Pick your marker: X or O: ")


def player_X():
  global board_numbers
  player=input('\nPlace your marker "X" on the board: ')
  if player in board_numbers and player in positions:
    board_numbers=(board_numbers.replace(player, "X"))
  elif player not in board_numbers or player not in positions:
    while player not in board_numbers or player not in positions:
      player=input("type in proper number: ")
    board_numbers=(board_numbers.replace(player, "X"))
  print(board_numbers)

def player_O():
  global board_numbers
  player=input('\nPlace your marker "O" on the board: ')
  if player in board_numbers and player in positions:
    board_numbers=(board_numbers.replace(player, "O"))
  elif player not in board_numbers or player not in positions:
    while player not in board_numbers or player not in positions:
      player=input("type in proper number: ")
    board_numbers=(board_numbers.replace(player, "O"))
  print(board_numbers)

def computer_X():
  global board_numbers
  computer=random.choice(positions)
  if computer in board_numbers:
    board_numbers=(board_numbers.replace(computer, "X"))
  elif computer not in board_numbers:
    while computer not in board_numbers:
      computer=random.choice(positions)
    board_numbers=(board_numbers.replace(computer, "X"))
  print(board_numbers)
  
def computer_O():
  global board_numbers
  computer=random.choice(positions)
  if computer in board_numbers:
    board_numbers=(board_numbers.replace(computer, "O"))
  elif computer not in board_numbers:
    while computer not in board_numbers:
      computer=random.choice(positions)
    board_numbers=(board_numbers.replace(computer, "O"))
  print(board_numbers)


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


"""
chars = []
for line in board_numbers:
   for c in line:
       chars.append(c)
print (chars)
print(chars.index("9"))
"""



game=True

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
      computer_O()
      win_o()
      if game==False:
        break

    else:
      os.system('clear')
      computer_X()
      win_x()
      if game==False:
        break
      player_O()
      win_o()
      if game==False:
        break
    
    
   
      
    
    
    
    
  


