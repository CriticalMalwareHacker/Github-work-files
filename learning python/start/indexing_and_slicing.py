lst=['one','two','three','four','five']
#index number begins from
#      0     1      2 
print(lst[2])
#running using slicing, the last index is sliced of so the range becomes 0:1
print(lst[0:2])
#prints from the 2nd index all the way to the last one
print(lst[2::])
#negative indexing prints it backwards
print(lst[-2::])

#using strings prints the letter the index position for example the last index is 4 so it prints 4
name = 'Tanay'
print(name[4])