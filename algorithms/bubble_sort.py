#My very own implementation of an bubble sorting
#by Timothy Joshua Dy Chua

def bubble_sort(mylist: list):
  for a in range(0, len(mylist)):
    for b in range(0, len(mylist)):
      if(mylist[a] < mylist[b]):
        placeholder = mylist[a]
        mylist[a] = mylist[b]
        mylist[b] = placeholder



  sorted_list = mylist
  return sorted_list


if __name__ == "__main__":


      mylist = [1, 120, 32, 4, 5, 29, 13, 21, 8]
      print(bubble_sort(mylist))
