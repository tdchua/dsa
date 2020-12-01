#My very own implementation of an AVL tree
#by Timothy Joshua Dy Chua
class AVLTreeNode:
  def __init__(self, val):
    self.val = val
    self.left  = None
    self.right = None

  def __str__(self, level=0):
    ret = "\t"*level+repr(self.val)+"\n"
    self.children = []
    if(self.left != None):
      self.children.append(self.left)
    if(self.right != None):
      self.children.append(self.right)

    for child in self.children:
      ret += child.__str__(level+1)
    return ret

  def __repr__(self):
    return '<tree node representation>'

  def _get_height(self):
    return self.height

  def _check_balance(self):
    print("Checking Balance of: ", self.val)

    if(getHeight(self.left) - getHeight(self.right) == 2): #If it is left heavy
      if(getHeight(self.left.left) - getHeight(self.left.right) < 0): #L-R Imbalance
        print("L-R Imbalance")
        self.left = self.left.LeftRotation()
        return self.RightRotation()
      else: #Just L Imbalance
        print("Left Imbalance!")
        return self.RightRotation()
    elif(getHeight(self.left) - getHeight(self.right) == -2): #Right heavy
      if(getHeight(self.right.left) - getHeight(self.right.right) > 0): #R-L Imbalance
        print("R-L Imbalance")
        self.right = self.right.RightRotation()
        return self.LeftRotation()
      else: #Just R Imbalance
        print("Right Imbalance!")
        return self.LeftRotation()

    else:
      return self

  def LeftRotation(self):
    if(self.right != None):
      nodeRight = self.right
      self.right = nodeRight.left
      nodeRight.left = self
      print("After left rotation, returning:", nodeRight.val)
      return nodeRight

  def RightRotation(self):
    if(self.left != None):
      nodeLeft = self.left
      self.left = nodeLeft.right
      nodeLeft.right = self
      return nodeLeft




class AVLTree:
  def __init__(self, root=None):
    self.root = root

  def insert(self, val):
    if(self.root != None):
      self.root = self._insert(self.root, val, None)
    else:
      self.root = AVLTreeNode(val)

  def _insert(self, root, val, parent):
    direction = ""
    if(root.val > val): #If the val to be inserted is smaller than our root val
      direction = "L"
      if(root.left == None):
        root.left = AVLTreeNode(val)
      else:
        root.left = self._insert(root.left, val, root)
    elif(root.val < val): #If the val to be inserted is bigger than our root val.
      direction = "R"
      if(root.right == None):
        root.right = AVLTreeNode(val)
      else:
        root.right = self._insert(root.right, val, root)

    #After updating the height and bf, we then apply check balance to make sure our nodes stay balanced after insertion.
    root = root._check_balance()
    print("New Node: ", root.val)

    return root

  def find_max(self, curr_node):
    if(curr_node.right == None):
      return curr_node
    else:
      return self.find_max(curr_node.right)


  def deletion(self, val):

    nodeToRemove = self.root
    path_nodes = []
    while(nodeToRemove != None and nodeToRemove.val != val):
      path_nodes.append(nodeToRemove)
      parent_node = nodeToRemove
      if(nodeToRemove.val < val): #val is bigger than the current node.
        nodeToRemove = nodeToRemove.right
      else:
        nodeToRemove = nodeToRemove.left

    node = nodeToRemove
    right_left_child = 0

    if(parent_node != 0):
      if(node.val < parent_node.val):
        right_left_child = 0 #current node is the left child
      if(node.val > parent_node.val):
        right_left_child = 1 #current node is the right child

    if(node.right != None and node.left != None): #Right and Left child nodes are present
      node_max_in_left = self.find_max(node.left) #This returns the highest val in the left subtree
      path_nodes.append(node_max_in_left)
      node_max_in_left.right = node.right
      if(parent_node != 0):
        if(right_left_child == 1):
          parent_node.right = node_max_in_left
        else:
          parent_node.left = node_max_in_right
      else: #If the root is the one to be removed
        self.root = node_max_in_left

    elif(node.right != None): #Right leaf only
      path_nodes.append(node.right)
      if(parent_node != 0): #There is a parent
        if(right_left_child == 1): #Node is the right child of parent node
          parent_node.right = node.right
        else:
          parent_node.left = node.right
      else: #This is the root node
        self.root = node.right

    elif(node.left != None): #Left leaf only
      path_nodes.append(node.left)
      if(parent_node != 0):
        if(right_left_child == 1):
          parent_node.right = node.left
        else:
          parent_node.left = node.left
      else: #This is the root node
        self.root = node.left


    #Tree after deletion
    print("After deletion")
    print(self.root)

    while(len(path_nodes) > 0):
      last_node = path_nodes.pop()
      last_node = last_node._check_balance()
      if(len(path_nodes) == 0):
        self.root = last_node
      else:
        if(last_node.val < path_nodes[-1].val):
          path_nodes[-1].left = last_node
        else:
          path_nodes[-1].right = last_node

    return 0


def getHeight(node):
  if(node == None):
    return 0
  else:
    return max(getHeight(node.left), getHeight(node.right)) + 1


if __name__ == "__main__":

  my_nodes_to_insert = [1, 5, 2, 10, 31, 40, 45, 56, 70]

  myAVLTree = AVLTree()
  for val in my_nodes_to_insert:
    print("Inserting: ", val)
    myAVLTree.insert(val)

    #Traversal!
    print(myAVLTree.root)

  print("Before deletion")
  print(myAVLTree.root)

  print("Let's try removing one node")
  myAVLTree.deletion(40)

  print(myAVLTree.root)

  print("Finished")
