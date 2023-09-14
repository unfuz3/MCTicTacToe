import numpy
from time import sleep
from classes import *

FIGDIC = { # Used to translate board's numbers to characters
	0:"_",
	1:"X",
	-1:"O",
	"draw":"Empate"
}

def getinput(prompt): # Safe way to get user's input for moves
  while True:
    response = input(prompt)
    try:
      return int(response)
    except ValueError:
      print("Por favor, escribe un numero")

def printboard(board:list[list[int]]) -> None: # Prints the board state
	for row in board:
		for sq in row:
			print(FIGDIC[sq],end="")
		print()

def isvalid(board:list[list[int]], pos:tuple[int,int]) -> bool: # Check whether a play is valid
	return (board[pos[0]][pos[1]]==0)

def wincheck(board:list[list[int]]) -> int: # Checks if any player won / Returns 0 if no one won
	boardmat = numpy.matrix(board) # Turn array into matrix to check wins by adding rows, cols, or diags
	
	# Check for horizontal win
	for row in boardmat * numpy.matrix([[1],[1],[1]]): 
		if 3 in row:
			return 1
		elif -3 in row:
			return -1
		
	# Check for vertical win
	for col in boardmat.transpose() * numpy.matrix([[1],[1],[1]]): 
		if 3 in col:
			return 1
		elif -3 in col:
			return -1
		
	# Check for diagonal wins
	diag1 = sum(numpy.diag(boardmat))
	diag2 = sum(numpy.diag(numpy.fliplr(boardmat)))

	if abs(diag1)==3:
		return numpy.sign(diag1)
	if abs(diag2)==3:
		return numpy.sign(diag2)
	
	return 0

def maketurn(board:list[list[int]],player:int,move:tuple[int,int]) -> tuple[bool,list[list[int]]]:
	if not isvalid(board,move):
		return (False,board)
	else:
		board[move[0]][move[1]]=player
		return (True,board)
	
def isdraw(board:list[list[int]]) -> bool:
	draw = True
	for i in range(3):
		for j in range(3):
			if isvalid(board,(i,j)):
				draw = False
	return draw

def main() -> None: # Main game loop
	board = numpy.full((3,3),0)
	turn = 1
	winner = 0
	print("Bienvenido al 3 en raya. Comienzan las X")
	sleep(0.5)
	while not winner:
		res = False
		printboard(board)
		if isdraw(board):
			winner = "draw"
			break
		while not res:
			row = getinput("Selecciona una fila: ")-1
			col = getinput("Selecciona una columna: ")-1
			res,board = maketurn(board,turn,(row,col))
			winner = wincheck(board)
			if not res:
				print("Movimiento invalido")
		turn *= -1
	print(f"El ganador es: {FIGDIC[winner]}")


if __name__=="__main__":
	pass