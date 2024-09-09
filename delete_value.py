quantity =input("enter the total number of list : ")
list =[]
for i in range(int(quantity)):
    list.append(int(input("enter element : ")))

delete_element = int(input("enter the element to delete : "))
for i in list:
    if (i == delete_element):
        list.remove(delete_element)
        print("the element has been deleted successfully and the new list is : ",list)
        break
    
    else:
     print("the value you want to delete is not in the list")
    
