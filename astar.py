import heapq, copy, time
import networkx as nx

class Stack:
	def __init__(self, stack, backwardCost): 
		self.pancakeStack = stack
		self.numPancakes = len(stack) - 1
		self.backwardCost = backwardCost
		self.forwardCost = self.calculateForwardCost()
		self.total = self.forwardCost + self.backwardCost

	# prints stack state
	def print(self):
		stackState = "Stack: "
		for i in range((self.numPancakes)):
			stackState += str(self.pancakeStack[i]) + " "
		print(stackState)

	# forward cost based on the gap heuristic
	def calculateForwardCost(self):
		forwardCost = 0
		for idx in range(self.numPancakes):
			gap = self.pancakeStack[idx] - self.pancakeStack[idx + 1]
			if gap < -1 or gap > 1:
				forwardCost += 1
		return forwardCost

	# flips stack at pancake
	def flipStack(self, index):
		self.pancakeStack[index:5] = reversed(self.pancakeStack[index:5])
		print("Pancake stack is ", self.pancakeStack, "after flipping pancake at ", index)

	# iterates cost after a flip
	def nextPancakeCost(self):
		self.backwardCost = self.backwardCost + 1

	# checks if the pancakes are in the goal state
	def isSolution(self):
		for x in range(self.numPancakes):
			if(self.pancakeStack[x] > self.pancakeStack[x+1]):
				return False
		return True

	# less than operator overload
	def __lt__(self, other):
		return self.total < other.total


class PriorityQueue:   
    def __init__(self): 
        self.queue = [] 

    # inserts an element into queue
    def insert(self, data, prio): 
        heapq.heappush(self.queue, (prio, data))
  
    # pops an element based on priority
    def pop(self): 
        try: 
        	return heapq.heappop(self.queue)[1]
        except IndexError: 
            exit() 

    # checks if queue is empty
    def isEmpty(self): 
       return len(self.queue) == []

def checkChildren(curr, visited, cost, graph, frontier):
	for pancake in range(curr.numPancakes):
		time.sleep(2)
		potentialFlip = copy.deepcopy(curr)
		potentialFlip.nextPancakeCost()
		potentialFlip.flipStack(pancake+1)
		if(potentialFlip in visited):
			continue
		graph.add_node(potentialFlip)
		graph.add_edge(curr, potentialFlip)

		potentialFlipCost = potentialFlip.total
		# check if a better path was found

		if potentialFlipCost < cost[potentialFlip]:
			cost[potentialFlip] = potentialFlipCost
			frontier.insert(potentialFlip, potentialFlip.total)
			visited[potentialFlip] = curr	
		elif potentialFlip not in cost:
			cost[potentialFlip] = potentialFlipCost
			frontier.insert(potentialFlip, potentialFlip.total)
			visited[potentialFlip] = curr

def main():
	originalStack = [5,3,4,1,2]
	# originalStack = []
	# size = int(input("How many pancakes? "))
	# for i in range(0, size):
	# 	print("Pancake", i)
	# 	originalStack.append(int(input("Enter pancake's size: ")))

	goalState = copy.deepcopy(originalStack)
	goalState.sort(reverse=True)
	print("Beginning A star on the stack, goal state is", goalState, "\n")

	stack = Stack(originalStack, 0)
	frontier = PriorityQueue()
	frontier.insert(stack, stack.total)

	# print stack
	stackState = "Stack: "
	for i in range(stack.numPancakes):
		stackState += str(stack.pancakeStack[i]) + " "
	print(stackState)

	# cost and path arrays
	visited = {}
	cost = {}
	for i in range(stack.numPancakes):
		visited[i] = None
	for i in range(stack.numPancakes):
		cost[i] = 0

	graph = nx.Graph()
	graph.add_node(stack)

	while (frontier.isEmpty() == False):
		curr = frontier.pop()
		time.sleep(2)

		if (curr.isSolution() == True):
			cost = curr.backwardCost
			path = [curr]
			print("Initialized path to", curr)
			while curr in visited:
				curr = visited[curr]
				if curr == None:
					break
				print("Adding", curr, "to the path.")


		if stack == goalState:
			print("Reached goal state.")
			exit()

		checkChildren(curr, visited, cost, graph, frontier)


	print("Sorting finished.")


if __name__== "__main__":
	main()
