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

if __name__ == "__main__":

  mylist = [i for i in range(10)]

  #Here is where we instantiate a list



  print(mylist)
