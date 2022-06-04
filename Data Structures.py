#Author: Sharath Sunil 
#Github: https://github.com/Anonymous1846/Data-Structures-and-Algorithms-In-Python.git
#Description: All the implementations of the data structures in python



from platform import node
from tempfile import tempdir


class Stack:
    '''The class represents a stack data structure'''
    def __init__(self,size=None) -> None:
        self.stack_list=[]  #initializing an empty stack for adding elements
        self.size=size      #an optional size can be specified 
    
    def push(self,data:int)->None:
        '''This method adds an element to the stack and checks if the size is specified and if the stack is full'''
        if self.size:
            if len(self.stack_list)>=self.size:
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
    '''The class represents a singly linked list and encapsulates its methods'''
    def __init__(self) -> None:
        self.head=None
    
    def __repr__(self) -> str:
        '''.__repr__() method returns the string representation of the linked list
        eg:1->2->3->4->5'''
        return '->'.join(str(i) for i in self.to_list())
    
    def insert_beg(self,data:int)->None:
        '''The method inserts an element at the beginning of the linked list'''
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            self.head.next=new_node
        else:
            self.head=new_node
            
    def insert_end(self,data:int)->None:
        '''The method inserts an element at the end of the linked list'''
        new_node=Node(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
        else:
            self.head=new_node
            
    def to_list(self)->list:
        '''Convert the linked list to a list by traversing the linked list'''
        nodes=[]
        temp=self.head
        while temp.next:
            nodes.append(temp.data)
            temp=temp.next
        return nodes
    
    def traverse(self)->None:
        '''Traverse the linked list after converting to a list'''
        for i in self.to_list():
            print(i,end=" ")

    def find(self,data:int)->bool:
        '''The method returns True if the node is found else returns False'''
        temp=self.head
        while temp:
            if temp.data==data:
                return True
            temp=temp.next
        return False
    
if __name__ == "__main__":
    stack=Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    print(stack.pop())
    print(stack.peek())
                