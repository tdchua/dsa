#My very own implementation of a binary search tree!
#by Timothy Joshua Dy Chua

class Node: #Here we define a node to have right and left values.
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None


class BinarySearchTree: #The BST Class
  def __init__(self, root):
    self.root = root

  def insert_Node(self, currentNode, value):
    if(currentNode == None): #There is no root of the tree yet
      print("Checking")
      currentNode = Node(value)
    else: #The tree has already been instantiated
      if(value < currentNode.value): #Check the left side
        self.insert(currentNode.left, value)
      elif(value >= currentNode.value): #Check the right side
        self.insert(currentNode.right, value)


if __name__ == "__main__":

  #Let's start with something simple.
  #Let's create a binary search tree with the numbers from 1 to 10
  my_BST = BinarySearchTree(None)
  for number in range(1, 11):
    my_BST.insert(my_BST.root, number)


  #Let's try printing the root
  print(my_BST.root)
  print(my_BST.root.value)
