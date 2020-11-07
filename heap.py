#My very own implementation of a heap! Let's make it a min heap.
#by Timothy Joshua Dy Chua

# Start time 2:08



#Formulas for heap index are:
#Parent Index = (index-1)/2
#Left Child Index = 2*index+1
#Right Child Index = 2*index+2

def heap_insert(heap, to_insert):
  #first we add the variable to the end of the heap
  heap.append(to_insert)

  #We check if every parent before it is less than the value to be inserted
  index_of_insertion = len(heap) - 1
  i = (index_of_insertion-1)//2

  while(i >= 0):
    if(heap[index_of_insertion] < heap[i]):
      #The value of the inserted node is smaller than its parent
      #Swapping
      placeholder = heap[index_of_insertion]
      heap[index_of_insertion] = heap[i]
      heap[i] = placeholder

      #Continue to the next parent
      index_of_insertion = i
      i = (i-1)//2
    else:
      break


  return heap



def heap_deletion(heap, to_delete):
  idx_to_delete = heap.index(to_delete)
  idx_last_elem = len(heap) - 1
  val_last_elem = heap[idx_last_elem]
  #We pop the last element in the heap because that's what we're going to replace

  #Check if the last element is the one to delete
  if(idx_to_delete == idx_last_elem):
    heap.pop()

  #If element to delete is not the last then...
  else:
    heap[idx_to_delete] = val_last_elem
    heap.pop()
    idx = idx_to_delete

    while(2*idx + 1 < len(heap)): #Checks if left child is present
      idx_right_child = 2*idx + 2
      idx_left_child = 2*idx + 1
      idx_to_replace = idx_left_child

      if(2*idx + 2 < len(heap)): #Checks if right child is present
          idx_to_replace = idx_left_child if idx_left_child < idx_right_child else idx_right_child

      if(heap[idx] > heap[idx_to_replace]):
        placeholder = heap[idx_to_replace]
        heap[idx_to_replace] = heap[idx]
        heap[idx] = placeholder

      else:
        break

  return heap


if __name__ == "__main__":

  to_insert = [3, 9, 12, 7, 1]
  my_heap = []



  #Insertion
  for node in to_insert:
    heap_insert(my_heap,node)

  #After Insertion
  print("After Insertion")
  print(my_heap)

  #After Deletion
  print("After Deletion")
  print(heap_deletion(my_heap, 3))
