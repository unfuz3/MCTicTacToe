import copy

def isvalid(board:list[list[int]], pos:tuple[int,int]) -> bool: # Check whether a play is valid
	return (board[pos[0]][pos[1]]==0)

class Node():
	def __init__(self,parent) -> None:
		self.parent = parent
		self.children = list[Node] 
		self.value = 0
		self.winrate = [0,0]
		self.pos = [[0,0,0],[0,0,0],[0,0,0]]
	
	def __repr__(self) -> str:
		return f"Node := depth:{self.getDepth()}, value:{self.value}, winrate:{self.winrate}, pos:{self.pos}"
	
	def getDepth(self) -> int:
		if self.parent == None:
			return 0
		else:
			return self.parent.getDepth() + 1
	
	def setNewChild(self):
		newnode = Node(self)
		self.children.append(newnode)
		return newnode
	
	def childrenMoves(self) -> list[list[list[int]]]:
		totalmoves = []
		for node in self.children:
			totalmoves.append(copy.deepcopy(node.pos))
		return totalmoves

class MCTree():
	def __init__(self) -> None:
		self.root = Node(None)
	
	def getPossibleOffspring(self, node:Node, player:int) -> list[list[list[int]]]: # returns the list of all possible moves as a list of boards
		offspring = []
		for i in range(3):
			for j in range(3):
				trying = copy.deepcopy(node.pos)
				if isvalid(trying,(i,j)):
					trying[i][j] = player
					offspring.append(trying)
		return offspring
	
	def reproduce(self,node:Node,player:int):
		moves = self.getPossibleOffspring(node,player)
		for move in moves:
			newnode = node.setNewChild()
			newnode.pos = move
	
	def expandFullDepth(self,rootnode:Node,depth:int,turn:int):
		childrenmoves = rootnode.childrenMoves()
		for move in self.getPossibleOffspring(rootnode, turn):
			if not move in childrenmoves:
				newnode = rootnode.setNewChild()
				newnode.pos = move
		if depth <= 0:
			return True
		else:
			for node in rootnode.children:
				self.expandFullDepth(node,depth-1,-turn)

			


if __name__=="__main__":
	pass