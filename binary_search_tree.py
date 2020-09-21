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


  def deletion(self, value):
    parent_node = find_parent(value)
    node = find_node(value)

    if(parent_node == 0):
      self.root = None
    else:
      right_left_child = 0
      if(node.val < parent_node.val):
        right_left_child = 0
      if(node.val > parent_node.val):
        right_left_child = 1

      if(node.right != None and node.left != None): #Right and Left child nodes are present
        
      elif(node.right != None): #Right leaf only
        if(right_left_child == 1): #Node is the right child of parent node
          parent_node.right = node.right
        else:
          parent_node.left = node.right
      elif(node.left != None): #Left leaf only
        if(right_left_child == 1):
          parent_node.right = node.left
        else:
          parent_node.left = node.left



    return 0

  def find_parent(self, curr_node, value): #A helper function to find the parent of a node
    if(curr_node.left != None):
      if(curr_node.left.value == value):
        return curr_node
    if(curr_node.right != None):
      if(curr_node.right.value == value):
        return curr_node

    parent = 0
    if(curr_node.value > value):
      parent = self.find_parent(curr_node.left, value)
    elif(curr_node.value < value):
      parent = self.find_parent(curr_node.right, value)

    return parent


  def find_node(self, curr_node, value):
    if(curr_node == None):
      return 0
    else:
      result = 0
      if(curr_node.value == value):
        return curr_node
      elif(value < curr_node.value):
        result = self.find_node(curr_node.left, value)
      elif(value > curr_node.value):
        result = self.find_node(curr_node.right, value)

      return result

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

  #Parent Finding
  print("BST Parent Finding")
  print("Parent for 15 is :", (my_BST.find_parent(my_BST.root, 15)).value)

  #Node Finding
  print("BST Node Finding")
  print("Node for 15 is: ", my_BST.find_node(my_BST.root, 15))
  print("It has the ff value: ", my_BST.find_node(my_BST.root, 15).value)


  #Node Deletion
  print("BST Node Deletion")
  priont("Node 15 is being deleted...")
  my_BST.delete
