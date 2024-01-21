class BinarySearchTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, value):
        if root == None:
            root = BinarySearchTree(value)
            
            return root
        else:
            if root.value == value:
                return root
            elif value < root.value:
                root.left = self.insert(root.left, value)
            elif value > root.value:
                root.right = self.insert(root.right, value)
            return root

    def remove(self, root, value):
        if root == None:
            return None 
        
        if value == root.value:
            #Root no tiene hijos
            if root.left == None and root.right == None:
                return None
            
            #Root no tiene hijo izquierdo
            if root.left == None:
                return root.right
            
            #Root no tiene hijo derecho
            if root.right == None:
                return root.left
            
            nodoTemporal = root.right
            while nodoTemporal.left != None: #aqui vamos al hijo más a la izquierda del subárbol derecho
                nodoTemporal = nodoTemporal.left
            
            root.value = nodoTemporal.value
            root.right = self.remove(root.right, nodoTemporal.value)
            return root
        elif value < root.value:
            root.left = self.remove(root.left, value)
            return root
        else:
            root.right = self.remove(root.right, value)
            return root
        
    

        
   
        


    def preOrder(self, root):
        print(root.value, end=" ")
        if root.left != None:
            self.preOrder(root.left)
        if root.right != None:
            self.preOrder(root.right)


    
        
        


root = BinarySearchTree(100)
root.insert(root, 50)
root.insert(root, 25)
root.insert(root, 115)
root.insert(root, 110)
root.insert(root, 30)
root.insert(root, 60)
root.insert(root, 55)
root.insert(root, 125)


root.preOrder(root)
print("\n")



root.remove(root, 50)

root.preOrder(root)
print("\n")


