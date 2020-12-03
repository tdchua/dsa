#My very own implementation of a doubly linked list!
#by Timothy Joshua Dy Chua


class Node:
  def __init__(self, value):
    print("Node Created")
    self.value = value
    self.next = None
    self.prev = None

class DLinked_List:
  def __init__(self):
    self.head = None
    self.tail = None

  def traverse(self):
    curr_node = self.head
    while(True):
      if(curr_node != None):
        print(curr_node.value)
        curr_node = curr_node.next
      else:
        break

  #For a doubly linked list the reverse traversal is much easier to implement
  def reverse_traverse(self):
    curr_node = self.tail
    while(True):
      if(curr_node != None):
        print(curr_node.value)
        curr_node = curr_node.prev
      else:
        break

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
          curr_node.next.prev = prev_node
          return

  def insert_node(self, value):
    #In the DSA book, it was only mentioned that adding a node would be inserting it after the list's tail.
    prev_node = None
    if(self.head != None): #To check if there is no head
      curr_node = self.head
      while(True):
        if(curr_node.next == None):
          curr_node.prev =  prev_node
          curr_node.next = Node(value)
          return
        else:
          prev_node = curr_node
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
  my_doubly_linked_list = DLinked_List()
  #We connect the head pointer of the linked list to the first node
  my_doubly_linked_list.head = head

  for element in my_list[1:]:
    my_doubly_linked_list.insert_node(element)

  #We then traverse the link
  print("Traversal")
  curr_node = my_doubly_linked_list.head
  my_doubly_linked_list.traverse()

  #Reverse traversal
  print("Reverse Traversal")
  my_doubly_linked_list.reverse_traverse()

  #Deleting a node
  print("Node Deletion")
  my_doubly_linked_list.delete_node(0)
  my_doubly_linked_list.traverse()

  #Inserting a node
  print("Node Insertion")
  my_doubly_linked_list.insert_node(16)
  my_doubly_linked_list.traverse()
