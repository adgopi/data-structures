import ctypes

class Node(object):
    '''
    Node class to represent data
    '''
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
        

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList(object):
    '''
    Doubly linked list implementation
    '''
    def __init__(self):
        self.listlen = 0
        self.head = None
        self.tail = None
        self.travIter = None
    
    def length(self):
        '''
        Return current length of the linked list
        '''
        return self.listlen

    def isEmpty(self):
        return self.length() == 0

    def clear(self):
        '''
        Empty the linked list
        '''
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.next = trav.prev = None
            trav.data = None
            trav = next
        self.head = None
        self.tail = None
        trav = None
        self.listlen = 0

    def add(self, elem):
        self.addTail(elem)

    def addTail(self, elem):
        '''
        Adds elem at the tail of the list
        '''
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next
        
        self.listlen += 1
    
    def addHead(self, elem):
        '''
        Adds elem at the head of the list
        '''
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev
        
        self.listlen += 1

    def addAt(self, index, data):
        '''
        Adds data at the specified index in the list
        '''
        if index < 0:
            raise Exception('Negative index passed: ' + str(index))

        if index == 0:
            self.addHead(data)
            return
        
        if index == self.listlen:
            self.addTail(data)
            return

        temp = self.head
        for i in range(0, index-2):
            temp = temp.next

        newNode = Node(data, temp, temp.next)
        temp.next.prev = newNode
        temp.next = newNode

        self.listlen += 1

    def peekFirst(self):
        '''
        Peek at head data, if it exists
        '''
        if self.isEmpty():
            raise Exception('Empty list!')
        return self.head.data

    def peekLast(self):
        '''
        Peek at tail data, if it exists
        '''
        if self.isEmpty():
            raise Exception('Empty list!')
        return self.tail.data

    def removeHead(self):
        '''
        Removes the head node of the list
        '''
        if self.isEmpty():
            raise Exception('Empty list!')

        data = self.head.data
        self.head = self.head.next
        self.listlen -= 1

        if self.isEmpty():
            self.tail = None
        else: 
            self.head.prev = None
        
        return data

    def removeTail(self):
        '''
        Removes the tail node of the list
        '''
        if self.isEmpty():
            raise Exception('Empty list!')

        data = self.tail.data
        self.tail = self.tail.prev
        self.listlen -= 1
        
        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def __remove__(self, node):
        '''
        Remove node from the list
        '''
        if node.next == None:
            return self.removeTail()
        if node == self.head:
            return self.removeHead()

        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data

        # node.data = node.next = node = None
        node.data = None
        node.next = None
        node.prev = None
        node = None
        self.listlen -= 1

        return data

    def removeAt(self, index):
        '''
        Remove the node at index from the list
        '''
        if index < 0 or index >= self.listlen:
            raise IndexError("Index out of bounds")

        # singly linked list
        # we will split in half for doubly linked list
        # trav = self.head
        # for i in range (index):
        #     trav = trav.next

        if index < self.listlen / 2:
            i = 0
            trav = self.head
            while i != index:
                i += 1  
                trav = trav.next
        
        # Search from the back of the list
        else:
            i = self.listlen - 1
            trav = self.tail
            while i != index:
                i -= 1
                trav = trav.prev
            
        return self.__remove__(trav)

    def remove(self, obj):
        '''
        Remove a value obj from the list
        '''
        trav = self.head

        if obj is None:
            while trav is not None:
                if trav.data is None:
                    self.__remove__(trav)
                    return True
                trav = trav.next
        else:
            while trav is not None:
                if obj == trav.data:
                    self.__remove__(trav)
                    return True
                trav = trav.next

        return False

    def indexOf(self, obj):
        '''
        Find index of obj in the list
        '''
        index = 0
        trav = self.head
        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index
                trav = trav.next
                index += 1 
        else:
            while trav is not None:
                if obj == trav.data:
                    return index
                trav = trav.next
                index += 1 
        return -1

    def contains(self,obj):
        '''
        Check if value obj is present in the list
        '''
        return self.indexOf(obj) != -1

    def __iter__(self):
        self.travIter = self.head
        return self

    def __next__(self): 
        """
        To move to next element. 
        """
        # Stop iteration if limit is reached 
        if self.travIter is None:
            raise StopIteration 
        
        # Store current travIter.data 
        data = self.travIter.data
        self.travIter = self.travIter.next
    
        # Else increment and return old value 
        return data
    
    def __repr__(self):
        sb = ""
        sb = sb + '[ '
        trav = self.head
        while trav is not None:
            sb = sb + str(trav.data)
            if trav.next is not None:
                sb = sb + ', '
        
            trav = trav.next
        
        sb = sb + ' ]'
        
        return str(sb)

List = DoublyLinkedList()
for i in range(10):
    List.add(i)

print("List:                       " + List.__repr__())
List.remove(3)
print("After removing 3:           " + List.__repr__())
List.addAt(5,20)
print("After adding 20 at index 5: " + List.__repr__())
List.addHead("newHead")
print("List after adding new head: " + List.__repr__())
List.addTail("newTail")
print("List after adding new tail: " + List.__repr__())
print("List contains 7? :          " + str(List.contains(7)))
print("Index of 20? :              " + str(List.indexOf(20)))
print("List empty? :               " + str(List.isEmpty()))
List.clear()
print("List after clearing:        " + List.__repr__())
print("List empty? :               " + str(List.isEmpty()))
