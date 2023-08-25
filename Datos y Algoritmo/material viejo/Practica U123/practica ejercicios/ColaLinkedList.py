from __future__ import annotations

class Node:
    __value: int
    __next:Node|None 

    def __init__(self, value):
        self.__value=value
        self.__next=None

    def getValue(self):
        return self.__value
    
    def getNext(self):
        return self.__next
    
    def setNext(self,next):
        self.__next=next

class Cola:
    __items=None
    __head=None
    __size:int=0

    def __init__(self):
        self.__items
        self.__head
        self.__size
    
    def insert(self,item):
        mynode=Node(item)
        
        if self.__size==0:
            self.__items=mynode
            self.__head=mynode
            self.__size+=1

        else:
            self.__head.setNext(mynode) #type: ignore
            self.__head=self.__head.getNext() #type: ignore
            self.__size+=1
    
    def supress(self):
        if self.__size==0:
            print("Error: No hay mas elementos")
        
        else:
            self.__items=self.__items.getNext()
            self.__size-=1


    def watch(self):
        mynode=self.__items
        while mynode!=None:
            print(mynode.getValue())
            mynode=mynode.getNext()
        



if __name__=="__main__":
    ps=Cola()    
    ps.insert(1)
    ps.insert(2)
    ps.insert(3)
    ps.insert(4)
    ps.supress()
    ps.watch()