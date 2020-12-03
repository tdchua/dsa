#My very own implementation of an merge sorting
#by Timothy Joshua Dy Chua

def merge_sort(mylist: list):
  if(len(mylist) == 1):
    return mylist
  else:
    midpoint = len(mylist)//2
    left_split =  mylist[0:midpoint]
    right_split = mylist[midpoint:]

    sorted_list = []
    left_side = merge_sort(left_split)
    right_side = merge_sort(right_split)

    while(len(left_side) > 0 or len(right_side) > 0):
      if(len(left_side) > 0 and len(right_side) > 0): #There are still elements in both lists
        left_val = left_side[0]
        right_val = right_side[0]
        if(left_val < right_val):
          left_val = left_side.pop(0)
          sorted_list.append(left_val)
        else:
          right_val = right_side.pop(0)
          sorted_list.append(right_val)
      elif(len(left_side) > 0):
        left_val = left_side.pop(0)
        sorted_list.append(left_val)
      elif(len(right_side) > 0):
        right_val = right_side.pop(0)
        sorted_list.append(right_val)

    return sorted_list


if __name__ == "__main__":

  mylist = [1, 120, 32, 4, 5, 29, 13, 21, 8]
  print(merge_sort(mylist))
