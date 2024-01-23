class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def addNode(self, value):
        nodoAAgregar = Node(value)
        if self.head == None and self.tail == None:
            self.head = nodoAAgregar
            self.tail = nodoAAgregar
        else:
            self.tail.next = nodoAAgregar
            self.tail = nodoAAgregar
        self.len +=1

    def addAtBegin(self, value):
        nodoAAgregar = Node(value)
        if self.head == None:
            self.head = nodoAAgregar
        else:
            nodoAAgregar.next = self.head
            self.head = nodoAAgregar
        self.len +=1


    #  0  1  2  3  4  5  6 <-- indexes
    # 10 11 12 13 14 15 16
    #  1  2  3  4  5  6  7 <-- positions

    def addAtIndex(self, value, index):
        nodoAAgregar = Node(value)
        current = self.head
        if index > (self.len - 1):
            print("No hay suficiente espacio")
            return
        elif index == 0:
            self.addAtBegin(value)
            
            return
        else:
            for i in range(index - 1):
                current = current.next
            nodoAAgregar.next = current.next
            current.next = nodoAAgregar
            self.len += 1

        
            


    def deleteHead(self):
        if self.head == None and self.tail == None:
            return
        self.head = self.head.next
        self.len -= 1



    def deleteTail(self):
        if self.tail == None:
            return
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.len -= 1




    def imprimirLinkedList(self):
        if self.head == None and self.tail == None:
            print("No hay elementos en la linked list")
            return
        current = self.head
        print(f"Tamaño: {self.len}. Imprimimos linked list: " , end="")
        while current != None:
            print(current.value, end=" ")
            current = current.next
        print("")
            
        
        
            

        

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



head = LinkedList()
head.addNode(10)
head.addNode(11)
head.addNode(12)
head.addNode(13)
head.addNode(14)
head.addNode(15)
head.addNode(16)
head.imprimirLinkedList()
head.addAtBegin(1000)
head.imprimirLinkedList()
head.deleteHead()
head.imprimirLinkedList()

head.addAtIndex(10000, 6)
head.imprimirLinkedList()

head.deleteTail()
head.imprimirLinkedList()
        