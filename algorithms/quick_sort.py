#My very own implementation of an quick sorting
#by Timothy Joshua Dy Chua

def quick_sort(mylist: list):
  if(len(mylist) <= 1 ):
    return mylist
  else:
    #Getting the pivot index
    pivot_idx = len(mylist) // 2
    last_idx = len(mylist) - 1

    #Swapping the last value with the value at the pivot index
    placeholder = mylist[pivot_idx]
    mylist[pivot_idx] = mylist[last_idx]
    mylist[last_idx] = placeholder
    pivot = placeholder

    #Swapping values
    left_idx = 0
    right_idx = last_idx - 1

    print(mylist)
    print(pivot)
    print("L:", left_idx)
    print("R:", right_idx)

    while(left_idx <= right_idx):
      if(mylist[left_idx] > pivot and mylist[right_idx] < pivot):
        #We swap the values at left idx and right idx
        placeholder = mylist[left_idx]
        mylist[left_idx] = mylist[right_idx]
        mylist[right_idx] = placeholder
      if(mylist[left_idx] < pivot):
        left_idx += 1
      if(mylist[right_idx] > pivot):
        right_idx -= 1


    #We then swap the position of the pivot and the left idx
    placeholder = mylist[left_idx]
    mylist[left_idx] = mylist[last_idx]
    mylist[last_idx] = placeholder
    print(mylist)


    return quick_sort(mylist[0:left_idx]) + [mylist[left_idx]] + quick_sort(mylist[left_idx+1:])


if __name__ == "__main__":

  mylist = [1, 120, 32, 4, 5, 29, 13, 21, 8]
  print(quick_sort(mylist))
