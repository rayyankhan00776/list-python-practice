elements= int(input("enter the element of the list : "))
list_elements = []
for i in range(elements):
    list_data = int(input(f"Enter element {i+1}: "))
    list_elements.append(list_data)

total =0
for i in list_elements:
    total = total + i

print(f"The sum of all elements is: {total}")




