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

  #This insert method is for cases wherein there is no root yet.
  def insert(self, value):
    if(self.root == None):
      self.root = Node(value)
    else:
      self.insert_Node(self.root, value)

  def insert_Node(self, currentNode, value):
    if(value < currentNode.value): #Check the left side
      if(currentNode.left == None):
        currentNode.left = Node(value)
      else:
        self.insert_Node(currentNode.left, value)
    elif(value >= currentNode.value): #Check the right side
      if(currentNode.right == None):
        currentNode.right = Node(value)
      else:
        self.insert_Node(currentNode.right, value)
      # print(value)

  def traversal(self, curr_node, mode=0): #mode = 0-Preorder, 1-Postorder, 2-BFS
    if(mode == 0 or mode == None):
        #Implementation of Preorder traversal
        if(curr_node == None):
          return
        else:
          print(curr_node.value)
          self.traversal(curr_node.left)
          self.traversal(curr_node.right)

  def search(self, curr_node, value): #Search if a value is present in the tree or not.
    if(curr_node == None):
      return 0
    else:
      left_result = 0
      right_result = 0
      if(curr_node.value == value):
        return 1
      elif(value < curr_node.value):
        left_result = self.search(curr_node.left, value)
      elif(value > curr_node.value):
        right_result = self.search(curr_node.right, value)

      return left_result + right_result


if __name__ == "__main__":

  #Let's start with something simple.
  #Let's create a binary search tree with the numbers from 1 to 10
  my_BST = BinarySearchTree(None)
  my_list = [1,5,3,7,9,8,10,15,14,13,12,16]
  for number in my_list:
    my_BST.insert(number)


  #Let's try printing the root
  print("Root")
  print(my_BST.root)
  print(my_BST.root.value)

  #Preorder Traversal!
  print("Preorder Traversal")
  my_BST.traversal(my_BST.root, 0)

  #Search
  print("BST Search")
  print("Searching for 15: ", my_BST.search(my_BST.root, 15))
  print("Searching for 79: ", my_BST.search(my_BST.root, 79))
