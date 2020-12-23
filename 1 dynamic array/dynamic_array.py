import ctypes 

class DynamicArray(object): 
    ''' 
    Dynamic array class python implementation
    '''
    
    def __init__(self, size = 1): 
        '''
        Constructor, takes size as param, default size 1
        '''
        self.length = 0 # count of actual elements in the array
        self.capacity = 1 # maximum capacity of the array 
        self.elements = (size * ctypes.py_object)() 
        
    def __len__(self): 
        """ 
        Return number of elements sorted in array 
        """
        return self.length 
        
    def __getitem__(self, k): 
        """ 
        Return element at index k 
        """
        if not 0 <= k <self.length: 
            # Check it k index is in bounds of array 
            return IndexError('K is out of bounds !') 
        
        return self.elements[k] # Retrieve from the array at index k 
        
    def append(self, ele): 
        """ 
        Add element to end of the array 
        """
        if self.length == self.capacity: 
            # Double capacity if not enough room 
            self._resize(2 * self.capacity) 
        
        self.elements[self.length] = ele # Set self.length index to element 
        self.length += 1

    def insertAt(self,item,index): 
        """ 
        This function inserts the item at any specified index. 
        """

        
        if index<0 or index>self.length: 
            print("please enter appropriate index..") 
            return
        
        if self.length==self.capacity: 
            self._resize(2*self.capacity) 
            
        
        for i in range(self.length-1,index-1,-1): 
            self.elements[i+1]=self.elements[i] 
            
        
        self.elements[index]=item 
        self.length+=1


        
    def delete(self): 
        """ 
        This function deletes item from the end of array 
        """

        if self.length==0: 
            print("Array is empty deletion not Possible") 
            return
        
        self.elements[self.length-1]=0
        self.length-=1
        
        
        
        
    def removeAt(self,index): 
        """ 
        This function deletes from a specified index. 
        """     

        if self.length==0: 
            print("Array is empty, deletion not Possible") 
            return
                
        if index<0 or index>=self.length: 
            return IndexError("Index out of bounds, deletion not possible")         
        
        if index==self.length-1: 
            self.elements[index]=0
            self.length-=1
            return      
        
        for i in range(index,self.length-1): 
            self.elements[i]=self.elements[i+1]            
            
        
        self.elements[self.length-1]=0
        self.length-=1

        
    def _resize(self, new_capacity): 
        """ 
        Resize internal array to capacity new_capacity 
        """
        
        temp = DynamicArray(new_capacity) # New array 
        
        for k in range(self.length): # Reference all existing values 
            temp.elements[k] = self.elements[k] 
            
        self.elements = temp.elements # Call temp the new array 
        self.capacity = new_capacity # Reset the capacity 

test_array = DynamicArray()
print(test_array.elements[:test_array.length])
# Can be replaced with assigning test_array.elements = [1,2,3,4,5,6] 
# but that will not update length
test_array.append(1)
test_array.append(2)
test_array.append(3)
test_array.append(4)
test_array.append(5)
test_array.append(6)
print(test_array.elements[:test_array.length])
test_array.delete()
test_array.delete()
test_array.delete()
print(test_array.elements[:test_array.length])