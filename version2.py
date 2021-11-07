"""
Min Heap Implementation in Python
"""
class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        while i // 2 > 0:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # Move the index to the parent to keep the properties
            i = i // 2
 
    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def minElement(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return None
        return self.heap_list[1]
    
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list
 
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
 
        # Return the min value of the heap
        return root

def performMove(my_heap):
    global elementInHeap
    global shouldOrder
    global moveCount
    if shouldOrder == 1:
        moveCount+=1
        shouldOrder=0
    my_heap.delete_min()
    elementInHeap-=1
    return my_heap

def performAdd(my_heap, sight_id):
    global elementInHeap
    global shouldOrder
    if elementInHeap>0:
        if int(sight_id)>int(my_heap.minElement()):
            shouldOrder=1
    my_heap.insert(sight_id)
    elementInHeap+=1
    return my_heap

def solution(my_heap, command, sight_id=None):
    if 'add' in command:
        return performAdd(my_heap, sight_id)
    else:
        return performMove(my_heap)

elementInHeap=0  
shouldOrder = 0
moveCount = 0

if __name__ == '__main__':
    n = int(input())
    my_heap = MinHeap()
    moveCount = 0

    for i in range(0,n*2):
        cmd = input()
        if 'add' in cmd:
            parsedCommand, sight_id = cmd.split(' ')
        else:
            parsedCommand=cmd
        my_heap = solution(my_heap, parsedCommand, sight_id)
    print(moveCount)
        

