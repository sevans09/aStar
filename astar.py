import heapq, copy, time

class Stack:
	def __init__(self, stack, backwardCost, goalState): 
		self.pancakeStack = stack
		self.numPancakes = len(stack) 
		self.backwardCost = backwardCost
		self.forwardCost = self.calculateForwardCost()
		self.total = self.forwardCost + self.backwardCost
		self.goalState = goalState

	# prints stack state
	def print(self):
		stackState = "Stack: "
		for i in range((self.numPancakes)):
			stackState += str(self.pancakeStack[i]) + " "
		print(stackState)

	# forward cost based on the gap heuristic
	def calculateForwardCost(self):
		forwardCost = 0
		for idx in range(self.numPancakes - 1):
			gap = self.pancakeStack[idx] - self.pancakeStack[idx + 1]
			if gap < -1 or gap > 1:
				forwardCost += 1
		return forwardCost

	# flips stack at pancake
	def flipStack(self, index):
		self.pancakeStack[index:self.numPancakes] = reversed(self.pancakeStack[index:self.numPancakes])
		print("Pancake stack is ", self.pancakeStack, "after flipping pancake at ", index)
		if self.pancakeStack == self.goalState:
			print("\nReached goal state.")
			print("Total cost was", self.total,"\n")
			exit()

	# iterates cost after a flip
	def nextPancakeCost(self):
		self.backwardCost = self.backwardCost + 1

	# checks if the pancakes are in the goal state
	def isSolution(self):
		for x in range(self.numPancakes - 1):
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

def checkChildren(curr, visited, cost, frontier):
	index = 0
	for pancake in range(curr.numPancakes):
		time.sleep(2)
		potentialFlip = copy.deepcopy(curr)
		potentialFlip.nextPancakeCost()
		potentialFlip.flipStack(pancake)

		potentialFlipTotal = potentialFlip.total
		potentialFlipForward = potentialFlip.forwardCost
		potentialFlipBack = potentialFlip.backwardCost

		# check if a better path was found
		if potentialFlip not in cost or potentialFlipCost < cost[potentialFlip]:
			cost[potentialFlip] = potentialFlipTotal
			print("Flip at ", index, "has a forward cost of", potentialFlipForward)
			print("Total cost is", potentialFlipTotal)
			frontier.insert(potentialFlip, potentialFlip.total)
			visited[potentialFlip] = curr
		index += 1
		

def main():
	originalStack = [5,4,3,1,2]

	originalStack = [5,2,1,4,3]

	goalState = copy.deepcopy(originalStack)
	goalState.sort(reverse=True)
	print("Beginning A star on the stack, goal state is", goalState, "\n")

	stack = Stack(originalStack, 0, goalState)
	frontier = PriorityQueue()
	frontier.insert(stack, stack.total)

	# print stack
	stackState = "Original stack: "
	for i in range(stack.numPancakes):
		stackState += str(stack.pancakeStack[i]) + " "
	print(stackState)

	# cost and path arrays
	cost = {}
	visited = {}
	length = stack.numPancakes

	for i in range(length):
		visited[i] = None
	for i in range(length):
		cost[i] = 0

	while (frontier.isEmpty() == False):
		curr = frontier.pop()
		time.sleep(1)
		checkChildren(curr, visited, cost, frontier)


if __name__== "__main__":
	main()
