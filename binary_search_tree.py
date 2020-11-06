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

  def traversal(self, curr_node, mode=0, to_explore=[]): #mode = 0-Preorder, 1-Postorder, 2-Inorder, 3-BFS
    if(mode == 0 or mode == None):
        #Implementation of Preorder traversal
        if(curr_node == None):
          return
        else:
          print(curr_node.value)
          self.traversal(curr_node.left, 0)
          self.traversal(curr_node.right, 0)

    elif(mode == 1):
      #Implementation of Postorder traversal
      if(curr_node == None):
        return
      else:
        self.traversal(curr_node.left, 1)
        self.traversal(curr_node.right, 1)
        print(curr_node.value)

    elif(mode == 2):
      #Implementation of Inorder traversal
      if(curr_node == None):
        return
      else:
        self.traversal(curr_node.left, 2)
        print(curr_node.value)
        self.traversal(curr_node.right, 2)

    elif(mode == 3):
      #Implementation of BFS traversal
      if(curr_node == None):
        return
      else:
        print(curr_node.value)
        if(curr_node.left != None):
          to_explore.append(curr_node.left)
        if(curr_node.right != None):
          to_explore.append(curr_node.right)

        #Time to explore
        if(len(to_explore) != 0):
          self.traversal(to_explore[0],3, to_explore[1:])



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
    parent_node = self.find_parent(self.root, value)
    node = self.find_node(self.root, value)

    right_left_child = 0
    if(parent_node != 0):
      if(node.value < parent_node.value):
        right_left_child = 0 #current node is the left child
      if(node.value > parent_node.value):
        right_left_child = 1 #current node is the right child

    if(node.right != None and node.left != None): #Right and Left child nodes are present
      node_max_in_left = self.find_max(node.left) #This returns the highest value in the left subtree
      node_max_in_left.right = node.right
      if(parent_node != 0):
        if(right_left_child == 1):
          parent_node.right = node_max_in_left
        else:
          parent_node.left = node_max_in_right
      else: #If the root is the one to be removed
        self.root = node_max_in_left

    elif(node.right != None): #Right leaf only
      if(parent_node != 0): #There is a parent
        if(right_left_child == 1): #Node is the right child of parent node
          parent_node.right = node.right
        else:
          parent_node.left = node.right
      else: #This is the root node
        self.root = node.right

    elif(node.left != None): #Left leaf only
      if(parent_node != 0):
        if(right_left_child == 1):
          parent_node.right = node.left
        else:
          parent_node.left = node.left
      else: #This is the root node
        self.root = node.left

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


  def find_node(self, curr_node, value): #Helper function to find the reference of the node.
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

  def find_min(self, curr_node):
    if(curr_node.left == None):
      return curr_node
    else:
      return self.find_min(curr_node.left)

  def find_max(self, curr_node):
    if(curr_node.right == None):
      return curr_node
    else:
      return self.find_max(curr_node.right)


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

  #Traversal!
  print("Preorder Traversal")
  my_BST.traversal(my_BST.root, 0)

  print("Postorder Traversal")
  my_BST.traversal(my_BST.root, 1)

  print("Inorder Traversal")
  my_BST.traversal(my_BST.root, 2)

  print("BFS Traversal")
  my_BST.traversal(my_BST.root, 3)

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
  print("Node 15 is being deleted...")
  my_BST.deletion(9)
  print("Our new tree is")
  # my_BST.traversal(my_BST.root, 0)
