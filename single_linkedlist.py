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

    # We must traverse to the end of the linked list

if __name__ == "__main__":

  my_list = [i for i in range(10)]

  #Here is where we instantiate a single linked list.
  #We instantiate the head node first; we give it the first value
  head = Node(my_list[0])
  #We then instantiate the linked list
  my_singly_linked_list = SLinked_List()
  #We connect the head pointer of the linked list to the first node
  my_singly_linked_list.head = head

  for element in my_list[1:]:
    next_node = Node(element)
    head.next = next_node
    head = next_node

  #We then traverse the link
  print("Traversal")
  curr_node = my_singly_linked_list.head
  my_singly_linked_list.traverse()


  #Reverse traversal
  print("Reverse Traversal")
  my_singly_linked_list.reverse_traverse(my_singly_linked_list.head)
