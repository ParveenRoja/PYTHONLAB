l1=[5,10,15,"English","Jessy","Apple"]
l2=[3,5,8,1,4,0]
print ("1.  len()")
print ("2.  append()")
print ("3.  extend()")
print ("4.  insert()")
print ("5.  remove()")
print ("6.  pop()")
print ("7.  Reverse()")
print ("8.  min()")
print ("9.  max()")
print ("10. count()")
print ("11. sort()")
print ("12. index()")
print ("13. clear()")
print ("14. Multiplication()")
print ("15. concatenation()")
print ("16. Data type()")
print(l1)
print(l2)
choice=int(input("Enter your choice:"))
if(choice==1):
  a=int(input("Enter 1 to view the length of list 1 and 2 for list 2"))
  if(a==1):
    print("length of the list-1")
    print(len(l1))
  elif(a==2):
    print("length of the list-2")
    print(len(l2))
elif (choice==2):
  a=int(input("Enter 1 for number and enter 2 for character \n choice:"))
  if(a==1):
    n = int(input("Enter the Number to append"))
    print("append a item in a list")
    l1.append(n)
  elif(a==2):
    k = str(input("Enter the Value to append"))
    print("append a item in a list")
    l1.append(k)
  else:
    print("Invalid")
  print("Now printing the current list")
  print(l1)
elif (choice==3):
  c = int(input("Enter the number to Extend"))
  d = str(input("Enter the value to extend"))
  print("Adding one or more item in list")
  l1.extend([c,d])
  print("Now printing the current list")
  print(l1)
elif (choice==4):
  d = int(input("Enter the position"))
  ch=int(input("Enter 1 for number and enter 2 for character \n choice:"))
  if(a==1):
    a = int(input("Enter the Number to Insert"))
    print("adding a item in a list by specifying the position")
    l1.insert(d,c)
  elif(a==2):
    e = str(input("Enter the Value to Insert"))
    print("adding a item in a list by specifying the position")
    l1.insert(m,e)
  else:
    print("Invalid")
  print("Now printing the current list")
  print(l1)
elif (choice==5):
  a=int(input("Enter 1 for number to remove and enter 2 for character to remove \n choice:"))
  if(a==1):
    n = int(input("Enter the Number to Remove"))
    print("Removing a item in a list")
    l1.remove(n)
  elif(a==2):
    e = str(input("Enter the Value to Remove"))
    print("Removing a item in a list")
    l1.insert(e)
  else:
    print("Invalid")
  print("Now printing the current list")
  print(l1)
elif (choice == 6):
  n=int(input("Enter the position to pop the item in a list"))
  l1.pop(n)
  print("Now printing the current list")
  print(l1)
elif (choice ==7):
  a=int(input("Enter 1 to reverse list1 and enter 2 to reverse list2 \n choice:"))
  if(a==1):
    print("Reverse of the List1")
    l1.reverse()
    print("Now printing the current list")
    print(l1)
  elif(a==2):
    print("Reverse of the List2")
    l2.reverse()  
    print("Now printing the current list")
    print(l2)
  else:
    print("Invalid")
elif (choice ==8):
    print("Minimum of the List2")
    print(min(l2))  
    print("Now printing the current list")
    print(l2)
elif (choice ==9):
    print("Maximum of the List2")
    print(max(l2))
    print("Now printing the current list")
    print(l2)
elif (choice == 10):
    print("List 2")
    print(l2)
    n=int(input("Printing the occurrence"))
    print(l2.count(n))
elif (choice == 11):
    print("Sorting the list-2 in a order")
    l2.sort()
    print(l2)
elif (choice ==12):
  a=int(input("Enter 1 to view list1 and 2 to view list2"))
  if(a==1):
    print(" List1")
    print(l1)
    c=int(input("Enter 1 to type numbers and 2 to type characters"))
    if(c==1):
      n=int(input("Enter the value to find the index"))
      print(l1.index(n))
    elif(a==2):
      n=str(input("Enter the value to find the index"))
      print(l1.index(n))
  elif(a==2):
    print(" List2")
    print(l2)
    n=int(input("Enter the value to find the index"))
    print(l2.index(n))
  else:
    print("Invalid")
elif(choice ==13):
  a=int(input("Enter the 1 to clear list 1 and 2 for list 2"))
  if(a==1):
    print("Clearing the List 1")
    clear.l1()
  elif(a==2):
    print("Clearing the List 2")
    clear.l2()
elif (choice ==14):
  a=int (input("Enter 1 to multiply list2 or 2 to multiply list2"))
  if(a==1):
      n=int(input("Enter the no.of times to multiply the list"))
      print("Multiplying list-1")
      print ("l1*(n)")
  elif(a==2):
      n=int(input("Enter the no.of times to multiply the list"))
      print("Multiplying list-2")
      print ("l2*(n)")
  else:
      print("Invalid")
elif (choice ==15):
  print ("Concatenating two list")
  l3=l1+l2
  print ("After Concatenating",l3)
elif(choice ==16):
  a=int(input("Enter 1 to view the data type of list1 or 2 to view the data type of list2"))
  if(a==1):
      print(type(l1))
  elif(a==2):
    print (type(l2))
  else:
    print("Invalid")
