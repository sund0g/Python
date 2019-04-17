# 2 examples of how to reverse a singley linked list,
#   1. Iterative
#       Time/space complexity: O(n)
#   2. Recursive
#       Time/space complexity: O(n)
#
# Notes:
#   - The Node and LinkedList classes only have the minumum methods needed to
#     demonstrate the reversals.
#   - Creating separate lists, (1 & 2) because the reversal of the list is 
#     global.  

import sys

class Node:
    def __init__ (self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    
    def getData(self):
       return self.data

    def setData(self, data):
       self.data = data

    def getNextNode(self):
       return self.nextNode

    def setNextNode(self, data):
       self.nextNode = data
# end Node class

class LinkedList:
    # Constructor
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        # New nodes are added at the head of the list. This is the most
        # efficient method of adding to the list.
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True
    
    def printNode(self):
        current = self.head
        my_list =[]
        while current:
            print(current.data)
            current = current.getNextNode()

    def printList(self):
        current = self.head
        list = []
        while current:
            list.append(current.data)
            current = current.getNextNode()
        return list

    def reverseListIteratively(self):
        # Declare 3 pointers, previous, current, next
        previous = None
        current = self.head
        next = None

        # Iterate while current is not null/None
        while (current):
            # Set next to current.next
            next = current.getNextNode()
            # Set current.next to previous, i.e. reverse the link
            current.setNextNode(previous)
            # Move to the next node
            previous = current
            current = next

        # Initialize head
        self.head = previous

        return self.printList()

    def reverseListRecursively(self, current):

        if (current.getNextNode() is None):
            # At end of list. Make head the current node
            self.head = current
            # Pop out of the recursive call
            return None

        # Not at end of list, recurse
        self.reverseListRecursively(current.getNextNode())

        # Reverse the link
        current.getNextNode().setNextNode(current)
        # Set next to None/Null to pop the previous recursion
        current.setNextNode(None)

        return self.printList()
# end LinkedList class

def main():

    try:
        assert (len(sys.argv[1:]) > 1), "\nPlease enter a ' '-delimited list\n"
        
    except AssertionError as error:
        print (error)
        sys.exit(1)

    # Put the input list into a proper linked list
    list1 = LinkedList()
    list2 = LinkedList()

    # Reversing the input arguments because LinkedList nodes are always
    # added to the head of the list. This preserves the original order of
    # the input arguments.
    for arg in reversed(sys.argv[1:]):
        list1.addNode(arg)
        list2.addNode(arg)

    print(f"\nOriginal list:\t{list1.printList()}")

    print(f"iterative:\t{list1.reverseListIteratively()}")
    
    print(f"recursive:\t{list2.reverseListRecursively(list2.head)}")
# end main()

if __name__ == "__main__":
    main()
