import heapq, copy, time

class Stack:
    def __init__(self, stack, goalState): 
        self.pancakeStack = stack
        self.numPancakes = len(stack) 
        self.forwardCost = self.calculateForwardCost()
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
            print("Cost was", self.forwardCost)
            exit()

    # checks if the pancakes are in the goal state
    def isSolution(self):
        for x in range(self.numPancakes - 1):
            if(self.pancakeStack[x] > self.pancakeStack[x+1]):
                return False
        return True

    # less than operator overload
    def __lt__(self, other):
        return self.forwardCost < other.forwardCost


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

        # increment backward cost and check flipped stack
        potentialFlip = copy.deepcopy(curr)
        potentialFlip.flipStack(pancake)

        # get costs at this configuration
        potentialFlipForward = potentialFlip.forwardCost

        # check if this flip is not in the cost array
        if potentialFlip not in cost :
            cost[potentialFlip] = potentialFlipForward
            print("Flip at ", index, "has a forward cost of", potentialFlipForward)
            print("Forward cost is", potentialFlipForward)
            frontier.insert(potentialFlip, potentialFlip.forwardCost)
            visited[potentialFlip] = curr

        # check if a better path was found
        elif potentialFlipCost < cost[potentialFlip]:
            cost[potentialFlip] = potentialFlipForward
            print("Flip at ", index, "has a forward cost of", potentialFlipForward)
            print("Forward cost is", potentialFlipForward)
            print("This cost is less than previous path's.")
            frontier.insert(potentialFlip, potentialFlip.forwardCost)
            visited[potentialFlip] = curr

        index += 1
        

def main():
    originalStack = [5,4,3,1,2]

    goalState = copy.deepcopy(originalStack)
    goalState.sort(reverse=True)
    print("Beginning A star on the stack, goal state is", goalState, "\n")

    stack = Stack(originalStack, goalState)
    frontier = PriorityQueue()
    frontier.insert(stack, stack.forwardCost)

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
