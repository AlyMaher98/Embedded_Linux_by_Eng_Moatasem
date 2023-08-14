'''
Task01
Write a Python program to count the number 4 in a given list.
'''
list=[]
listlen =5
print("Enter the items of the list")
for i in range (listlen):
    x=input()
    list.append(x)
print("The 4th elemnt of the list is ",list[3])