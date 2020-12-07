#My very own implementation of an insertion sorting
#by Timothy Joshua Dy Chua

def insertion_sort(mylist: list):
  i = 0
  while(i < len(mylist)):
    j = 0
    while(j < i):
      if(mylist[i] < mylist[j]):
        to_insert = mylist[i]
        del(mylist[i])
        mylist.insert(j, to_insert)
        break

      j += 1
    i += 1
  return mylist


if __name__ == "__main__":

  mylist = [1, 120, 32, 4, 5, 29, 13, 21, 8]
  print(insertion_sort(mylist))
