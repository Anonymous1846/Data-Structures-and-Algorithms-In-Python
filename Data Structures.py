#Author: Sharath Sunil 
#Github: https://github.com/Anonymous1846/Data-Structures-and-Algorithms-In-Python.git
#Description: All the implementations of the data structures in python



class Stack:
    '''The class represents a stack data structure'''
    def __init__(self,size=None) -> None:
        self.stack_list=[]  #initializing an empty stack for adding elements
        self.size=size      #an optional size can be specified 
    
    def push(self,data:int)->None:
        '''This method adds an element to the stack and checks if the size is specified and if the stack is full'''
        if self.size:
            if size(self.stack_list)>=self.size:
                print("Stack Overflow")
                return
        self.stack_list.append(data)
    
    def pop(self)->int:
        '''This method removes an element from the stack and checks if the stack is empty'''
        if not self.stack_list:
            print("Stack Underflow")
            return
        return self.stack_list.pop()
    
    def peek(self)->int:
        '''This method returns the top element of the stack'''
        if not self.stack_list:
            print("Stack Underflow")
            return
        return self.stack_list[-1] #because it is last in first out ds
    
    def size(self)->int:
        '''.size() method returns the size of the stack'''
        return len(self.stack_list)

class Node:
    '''The Node class represents a node in a singly/doubly linked list'''
    def __init__(self,data) -> None:
        self.data=data
        self.next=None  
        self.prev=None  #applicable for doubly linked list
    def __repr__(self) -> str:
        return str(self.data)
    
    
class Singly_Linked_List:
    def __init__(self) -> None:
        self.head=None
    def insert_beg(self,data:int)->None:
        pass
if __name__ == "__main__":
    pass
                