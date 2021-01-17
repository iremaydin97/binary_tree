class Node:
    def __init__(self, data): #Self tüm hepsinde belirtilmektedir
        self.left = None #Sag ve sol kol boş olarak setlenmektedir
        self.right = None
        self.data = data #Karsilastirma yapacagimiz deger
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data: #Kucuk ise sola eklenir
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: #Buyuk ise saga eklenir
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data) #Burada yer alan print'in yer degistirmesiyle preorder,inorder ve postorder durumu cikar
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(25) #Kök dugum
root.insert(14) #Ekleme islemi yapar
root.insert(23)
root.insert(40)
root.insert(24)
root.insert(48)
root.insert(7)
root.insert(5)
root.insert(34)
root.insert(10)
root.insert(17)
root.insert(36)
root.PrintTree()
