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
        self.len = 0

    # inserts an element into queue
    def insert(self, data, prio): 
        heapq.heappush(self.queue, (prio, data))
        self.len += 1
  
    # pops an element based on priority
    def pop(self): 
        try: 
        	self.len -= 1
        	return heapq.heappop(self.queue)[1]
        except IndexError: 
            exit() 

    # checks if queue is empty
    def isEmpty(self): 
       return len(self.queue) == []

def checkChildren(curr, visited, frontier, currPathCost):
	index = 0
	for pancake in range(curr.numPancakes):
		#time.sleep(2)
		potentialFlip = copy.deepcopy(curr)
		potentialFlip.backwardCost = potentialFlip.backwardCost + 1
		potentialFlip.flipStack(pancake)

		potentialFlipForward = potentialFlip.calculateForwardCost()
		potentialFlipBack = potentialFlip.backwardCost
		potentialFlipTotal = potentialFlipBack + potentialFlipForward

		childInFrontier = False
		for i in range(frontier.len):
			if frontier.queue[i] == potentialFlip:
				print("Found")
				childInFrontier = True

		if childInFrontier == False and potentialFlip not in visited:
			print("in if")
			currPathCost = potentialFlipTotal
			print("Flip at ", index, "has a forward cost of", potentialFlipForward)
			print("Total cost is", potentialFlipTotal)
			frontier.insert(potentialFlip, potentialFlipTotal)
			visited.append(potentialFlip)
		
		elif potentialFlip in frontier and frontier[potentialFlip].calculateForwardCost() > potentialFlipTotal:
			print("here")

		index += 1
		

def main():
	originalStack = [5,4,3,1,2]

	# works for this
	originalStack = [5,2,1,4,3]

	originalStack = [1,2,3,5,4]

	originalStack = [1,3,2,4]

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

	# visited arrays
	length = stack.numPancakes
	visited = [None] * length

	while (frontier.isEmpty() == False):
		curr = frontier.pop()
		print("Frontier is", frontier.queue)
		time.sleep(1)
		currPathCost = 100
		checkChildren(curr, visited, frontier, currPathCost)


if __name__== "__main__":
	main()
