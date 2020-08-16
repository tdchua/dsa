#My very own implementation of a singly linked list!
#by Timothy Joshua Dy Chua


class Node:
  def __init__(self, value):
    print("Node Created")
    self.value = value
    self.next = None

class SLinked_List:
  def __init__(self):
    self.head = None

  def traverse(self):
    curr_node = self.head
    while(True):
      if(curr_node != None):
        print(curr_node.value)
        curr_node = curr_node.next
      else:
        break

  #I used recursion to perform this reverse traversal
  def reverse_traverse(self, mynode):
    if(mynode.next == None):
      print(mynode.value)
      return

    self.reverse_traverse(mynode.next)
    print(mynode.value)

    return

  def delete_node(self, value):
    #The case for head removal
    if(value == self.head.value):
      self.head = self.head.next
    else:
      curr_node = self.head
      while(True):
        prev_node = curr_node

        #If we have reached the end of the list
        if(curr_node.next == None):
          print("Node to delete...not found")
          return
        curr_node = curr_node.next

        #The node to remove is curr_node
        if(curr_node.value == value):
          prev_node.next = curr_node.next
          return

  def insert_node(self, value):
    #In the DSA book, it was only mentioned that adding a node would be inserting it after the list's tail.
    if(self.head != None): #To check if there is no head
      curr_node = self.head
      while(True):
        if(curr_node.next == None):
          curr_node.next = Node(value)
          return
        else:
          curr_node = curr_node.next
    else:
      self.head = Node(value)
      return


if __name__ == "__main__":

  my_list = [i for i in range(10)]

  #Here is where we instantiate a single linked list.
  #We instantiate the head node first; we give it the first value
  head = Node(my_list[0])
  #We then instantiate the linked list
  my_singly_linked_list = SLinked_List()
  #We connect the head pointer of the linked list to the first node

  for element in my_list[1:]:
    my_singly_linked_list.insert_node(element)

  #We then traverse the link
  print("Traversal")
  curr_node = my_singly_linked_list.head
  my_singly_linked_list.traverse()

  #Reverse traversal
  print("Reverse Traversal")
  my_singly_linked_list.reverse_traverse(my_singly_linked_list.head)

  #Deleting a node
  print("Node Deletion")
  my_singly_linked_list.delete_node(0)
  my_singly_linked_list.traverse()

  #Inserting a node
  print("Node Insertion")
  my_singly_linked_list.insert_node(16)
  my_singly_linked_list.traverse()
