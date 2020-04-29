import sys 
import random

class MaxHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = 1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos > (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def maxHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] < self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.maxHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.maxHeapify(self.rightChild(pos))
            # print(self.Heap) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] > self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        if self.size == 1:
             print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def maxHeap(self): 
  
        for pos in range(1, self.size//2 + 1): 
            self.maxHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.maxHeapify(self.FRONT) 
        return popped 


def karmarkar(S):
    length = len(S)
    maxHeap = MaxHeap(200)
    for i in range(length):
        maxHeap.insert(S[i])

    # condition to terminate is that both children of the max heap will be zeroes
    #the way we programmed, the left child is always smaller than the right child
    while maxHeap.Heap[2] != 0 or maxHeap.Heap[3] != 0:
        heap = maxHeap.Heap
        maximum = max(heap[2], heap[3])
        if maximum == heap[2]:
            maxHeap.Heap[1] = heap[1] - heap[2]
            maxHeap.Heap[2] = 0 
            maxHeap.maxHeapify(2)
            maxHeap.maxHeapify(1)

        else:
            maxHeap.Heap[1] = heap[1] - heap[3]
            maxHeap.Heap[3] = 0
            maxHeap.maxHeapify(3)
            maxHeap.maxHeapify(1)

    return(maxHeap.Heap[1])

# starting below are things Michael added

def repeatedRandom(S):
    length = len(S)
    minResidue = float("inf")

    # Creating a array of +1 and -1 randomly of length length
    R = []

    for i in range(25000):
        residue = 0
        # randomly assign each element to a list
        for i in range(length):
            rand_bit = random.choice([-1, +1])
            residue += S[i]*rand_bit
            R.append(rand_bit)

        residue = abs(residue)
        if residue < minResidue:
            minResidue = residue

    return minResidue
    

def hillClimbing(S):
    length = len(S)

    # Creating a array of +1 and -1 randomly of length length
    R = []
    residue = 0

    # determine the initial residue while generating random bits
    for i in range(length):
        rand_bit = random.choice([-1, +1])
        residue += S[i]*rand_bit
        R.append(rand_bit)
    
    for i in range(25000):
        randNum1 = random.randint(0, length - 1)
        randNum2 = random.randint(0, length - 1)

        # do a random move
        R[randNum1] = -1 * R[randNum1]
        rand_number = random.random()

        madeMove2 = False
        if rand_number>0.5:
            R[randNum2] = -1 * R[randNum2]
            madeMove2 = True
        
        # find the new residue
        new_res = 0
        for i in range(length):
            new_res += R[i]*S[i]

        # if new residue is less, then update residue
        if abs(new_res) < abs(residue):
            residue = abs(new_res)

        # if new residue is more, reverse the changes that were just made
        else:
            R[randNum1] = -1 * R[randNum1]
            if madeMove2 == True:
                R[randNum2] = -1 * R[randNum2]

    return residue


def simulatedA(S):
    import random
    import math

    length = len(S)

    # Creating a array of +1 and -1 randomly of length length
    R = []
    residue = 0

    # determine the initial residue while generating random bits
    for i in range(length):
        rand_bit = random.choice([-1, +1])
        residue += S[i]*rand_bit
        R.append(rand_bit)

    # make sure residue is positive
    residue = abs(residue)

    # keep track of the R that corresponds to the minimum residue so far
    Rlowest = R
    
    for i in range(25000):
        randNum1 = random.randrange(0, length - 1)
        randNum2 = random.randrange(0, length - 1)

        # do a random move
        R[randNum1] = -1 * R[randNum1]
        rand_number = (random.randint(0, 10000000) % 100) / 100

        madeMove2 = False
        if rand_number>0.5:
            R[randNum2] = -1 * R[randNum2]
            mademove2 = True
        
        # find the new residue
        new_res = 0
        for i in range(length):
            new_res += R[i]*S[i]

        # if new residue is less, then update residue
        if abs(new_res) < residue:
            residue = abs(new_res)

        # if new residue is more, reverse the changes that were just made but have a probability that the change is kept
        else:
            diff_in_residues = abs(new_res) - residue
            prob = math.exp(-diff_in_residues/((10**10)*(0.8)**(i / 300)))
            randNum3 = (random.randint(0, 10000000) % 100) / 100
            if randNum3 > prob: # notice that there's a probability that the changes will not be reversed even if it's not a helpful move
                R[randNum1] = -1 * R[randNum1]
                if madeMove2 == True:
                    R[randNum2] = -1 * R[randNum2]

        if residue > abs(new_res):
            Rlowest = R
            residue = abs(new_res)

    return residue

# Given array S provided in the inputfile and n, the length of array S, create a random solution using a prepartition.
def create_rand_solution_from_prepartition(S, n):
    # First, I create a prepartititon with n random integers each ranging from 0 to n.
    P = []
    Anew = [0]*n

    for i in range(n):
        rand_number = random.randrange(0, n)
        P.append(rand_number)
        index = P[i]
        Anew[index] += S[i]

    return Anew

def prepartitioned_repeated_random(S):
    n = len(S)
    R = create_rand_solution_from_prepartition(S, n)
    minResidue1 = abs(karmarkar(R))

    iterations = 25000
    for k in range(0, iterations):
        R_prime = create_rand_solution_from_prepartition(S, n) # see which random prepartition works best
        newResidue = abs(karmarkar(R_prime))
        if (newResidue < minResidue1):
            R = R_prime
            minResidue1 = newResidue

    return minResidue1

def createrandP(n):
    # First, I create a prepartititon with n random integers each ranging from 0 to n.
    P = []

    for i in range(n):
        rand_number = random.randrange(0, n)
        P.append(rand_number)

    return P

def createSolutionFromP(P, S):
    n = len(P)
    Anew = [0]*n

    for i in range(n):
        index = P[i]
        Anew[index] += S[i]

    return Anew
# print(createSolutionFromP([1,2,2,1]))


def prepartitioned_hill_climbing(S):
    n = len(S)
    R = createrandP(n)
    residue = abs(karmarkar(createSolutionFromP(R, S)))

    iterations = 25000
    for k in range(0, iterations):
        R_orig = R
        randNum1 = random.randint(0, n - 1)
        randNum1newLocation = random.randint(0, n - 1)

        randNum2 = random.randint(0, n - 1)
        randNum2newLocation = random.randint(0, n - 1)

        # do a random move
        R[randNum1] = randNum1newLocation # move to a different group
        rand_number = random.random()

        madeMove2 = False
        if rand_number>0.5:
            R[randNum2] = randNum2newLocation # move to a different group
            madeMove2 = True

        # now find new residue
        S_prime = createSolutionFromP(R, S)
        new_res = karmarkar(S_prime) # we might to represent the random moves differently

        # if new residue is less, then update residue
        if abs(new_res) < abs(residue):
            residue = abs(new_res)

        # if new residue is more, reverse the changes that were just made
        else:
            R = R_orig
    return residue

def prepartitioned_simulated_annealing(S):
    n = len(S)
    R = createrandP(n)
    Rlowest = R # keep track of the R that corresponds to the minimum residue so far
    residue = abs(karmarkar(createSolutionFromP(R, S)))

    iterations = 25000
    for k in range(0, iterations):
        R_orig = R
        randNum1 = random.randint(0, n - 1)
        randNum1newLocation = random.randint(0, n - 1)

        randNum2 = random.randint(0, n - 1)
        randNum2newLocation = random.randint(0, n - 1)

        # do a random move
        R[randNum1] = randNum1newLocation # move to a different group
        rand_number = random.random()

        madeMove2 = False
        if rand_number>0.5:
            R[randNum2] = randNum2newLocation # move to a different group
            madeMove2 = True

        # now find new residue
        S_prime = createSolutionFromP(R, S)
        new_res = karmarkar(S_prime) # we might to represent the random moves differently

        # if new residue is less, then update residue
        if abs(new_res) < abs(residue):
            residue = abs(new_res)

        # if new residue is more, reverse the changes that were just made but have a probability that the change is kept
        else:
            diff_in_residues = abs(new_res) - residue
            prob = math.exp(-diff_in_residues/((10**10)*(0.8)**(i / 300)))
            randNum3 = (random.randint(0, 10000000) % 100) / 100
            if randNum3 > prob: # notice that there's a probability that the changes will not be reversed even if it's not a helpful move
                R = R_orig

        if residue > abs(new_res):
            Rlowest = R
            residue = abs(new_res)

    return residue



# the following function generates a set of 100 random integers each of
# which is in the range (1, 10^12)
def random_number_generator():
    arr = []
    
    for i in range(100):
        rand_number = random.randrange(1, 10**12)
        arr.append(rand_number)

    return arr
  
# Driver Code 
if __name__ == "__main__": 
    pass
    array = []
    with open(sys.argv[3], 'r') as file:
        dimension = int(sys.argv[2])
        for line in file.readlines(): 
            line = int(line)
            array.append(line)
        if int(sys.argv[2]) == 0:
            result = karmarkar(array)
            print(result)
        if int(sys.argv[2]) == 1:
            result = repeatedRandom(array)
            print(result)
        if int(sys.argv[2]) == 2:
            result = hillClimbing(array)
            print(result)
        if int(sys.argv[2]) == 3:
            result = simulatedA(array)
            print(result)
        if int(sys.argv[2]) == 11:
            result = prepartitioned_repeated_random(array)
            print(result)
        if int(sys.argv[2]) == 12:
            result = prepartitioned_hill_climbing(array)
            print(result)
        if int(sys.argv[2]) == 13:
            result = prepartitioned_hill_climbing(array)
            print(result)





    # print(random_number_generator())


    # # maxHeap.Print() 
    # # print("The Min val is " + str(maxHeap.remove()))

    # print(karmarkar([2,1,4,3,6,5]))