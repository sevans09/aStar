import heapq, copy, time

class Stack:
    def __init__(self, stack, backwardCost, goalState): 
        self.pancakeStack = stack
        self.numPancakes = len(stack) 
        self.forwardCost = self.calculateForwardCost()
        self.goalState = goalState

    # less than operator overload
    def __lt__(self, other):
        return self.forwardCost < other.forwardCost
        
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
            print("\nReached goal state", self.pancakeStack)
            exit()


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

def checkChildren(curr, visited, frontier):
    pancakeIndex = 0

    # check each possible configuration of current stack
    for pancake in range(curr.numPancakes):
        time.sleep(1)
        potentialFlip = copy.deepcopy(curr)

        # after stack is flipped at given pancake's index, goal reached
        # is checked in flipStack function
        potentialFlip.flipStack(pancake)

        # get costs for this configuration
        potentialFlipForward = potentialFlip.calculateForwardCost()

        # ensure child (potential flip) is not in frontier or visited
        childInFrontier = False
        for i in range(frontier.len):
            if frontier.queue[i] == potentialFlip:
                childInFrontier = True

        if childInFrontier == False and potentialFlip not in visited:
            visited.append(potentialFlip)
            frontier.insert(potentialFlip, potentialFlipForward)
            print("\nFlip at ", pancakeIndex, "has a forward cost of", potentialFlipForward)


        # increment index to keep track of which pancake is being flipped
        pancakeIndex += 1
        

def main():
    print("Enter numbers separated by spaces: ")
    originalStack = list(map(int, input().split()))

    # getting goal state to reach
    goalState = copy.deepcopy(originalStack)
    goalState.sort(reverse=True)
    print("Beginning UCS on the stack, goal state is", goalState, "\n")

    # initializing frontier
    frontier = PriorityQueue()
    stack = Stack(originalStack, 0, goalState)
    frontier.insert(stack, stack.forwardCost)

    print ("\nOriginal stack is: ", originalStack, "\n")

    # visited array
    length = stack.numPancakes
    visited = [None] * length

    while (frontier.isEmpty() == False):
        curr = frontier.pop()
        checkChildren(curr, visited, frontier)


if __name__== "__main__":
    main()
