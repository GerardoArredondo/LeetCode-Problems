class BinaryTreeNode:
    def __init__(self, value = None, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def depthFirst(self, root):
        stack = []
        stack.append(root)
        while stack.__len__() != 0:
            acutal = stack.pop()
            print(acutal.value)

            if acutal.rightChild:
                stack.append(acutal.rightChild)
            if acutal.leftChild:
                stack.append(acutal.leftChild)

        

        
        



    


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
 


        
root.depthFirst(root)




    

