class BinaryTreeNode:
    def __init__(self, value = None, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def depthFirst(self, root):
        if root == None:
            return []
        stack = []
        arrayARetornar = []
        stack.append(root)
        while stack.__len__() != 0:
            acutal = stack.pop()
            arrayARetornar.append(acutal.value)
            
            if acutal.rightChild:
                stack.append(acutal.rightChild)
            if acutal.leftChild:
                stack.append(acutal.leftChild)
        
        return arrayARetornar
    
    def breathFirst(self, root):
        if root == None:
            return []
        queue = []
        arrayARetornar = []
        queue.append(root)
        while queue.__len__() != 0:
            nodoActual = queue.pop(0) #We use index 0 because we're using queue, if not for the zero, FIFO wouldn't be true 
            arrayARetornar.append(nodoActual.value)
            if nodoActual.leftChild != None:
                queue.append(nodoActual.leftChild)
            if nodoActual.rightChild != None:
                queue.append(nodoActual.rightChild)
        return arrayARetornar



        

child1 =  BinaryTreeNode(1)
child2 =  BinaryTreeNode(2)
child3 =  BinaryTreeNode(3)
child4 =  BinaryTreeNode(4)
child5 =  BinaryTreeNode(5)
child6 =  BinaryTreeNode(6)
child7 =  BinaryTreeNode(7)


root = BinaryTreeNode(10)
root.leftChild = child1
root.rightChild = child2
child1.leftChild = child3
child1.rightChild = child4
child2.leftChild = child5
child4.leftChild = child6
child4.rightChild = child7
 


        
print(f"En DFS el resultado es {root.depthFirst(root)}")
print(f"En BFS el resultado es {root.breathFirst(root)}")




    

