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
            # print(maxHeap.Heap)

    return (maxHeap.Heap[1])


# the following function generates a set of 100 random integers each of
# which is in the range (1, 10^12)
def random_number_generator():
    arr = []
    
    for i in range(100):
        rand_number = random.randrange(0, 10**12)
        arr.append(rand_number)

    return arr


# Given array S provided in the inputfile and n, the length of array S, create a random solution using a prepartition.
def create_rand_solution_from_prepartition(S):

    # First, I create a prepartititon with 100 random integers each ranging from 0 to 100.

    P = []
    
    for i in range(100):
        rand_number = random.randrange(0, 100)
        P.append(rand_number)
    A_prime = [0]*100
    # print(len(A_prime))
    for i in range(100):
        index = P[i]
        A_prime[index] += S[i]
    return A_prime

# print(create_rand_solution_from_prepartition([10,8,7,6,5], 5))




def prepartitioned_repeated_random(S):
    R = create_rand_solution_from_prepartition(S)

    max_iter = 15
    for i in range(0, max_iter):
        R_prime = create_rand_solution_from_prepartition(S)
        if (karmarkar(R_prime) < karmarkar(R)):
            R = R_prime
    return karmarkar(R)

# print(prepartitioned_repeated_random([10,8,7,6,5, 6,7,88,9,73]))







  
# Driver Code 
if __name__ == "__main__": 
    # array is the input array from the autograder.
    array = []
    with open(sys.argv[3], 'r') as file:
        for line in file.readlines(): 
            line = int(line)
            array.append(line)

        if int(sys.argv[2]) == 0:
            print(karmarkar(array))

        if int(sys.argv[2]) == 11:
            print(prepartitioned_repeated_random(array))


    # print(random_number_generator())

    # # maxHeap.Print() 
    # # print("The Min val is " + str(maxHeap.remove()))

    # print(karmarkar([2,1,4,3,6,5]))









