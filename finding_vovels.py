text = input("enter the  sentense in which ypu want to find vovels : ")
counter =0
for char in text:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        counter += 1

print(f"The number of vowels in the sentence is: {counter}")