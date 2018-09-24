#list1 = []
#list2 = []
#element_count = int(input("How many elements in the list? "))
#counter = 0
#while counter  < element_count:
#    elem = input("Enter an element to add to the list: ")
#    for i in range(len(list1)):
#        if list1[i] != (list1[i]-1)
#        list2.append(elem)
#    counter +=1
#
list1 = ['hello', 'hey','hello','hi']
list2 = list1
list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        for k in range(len(list3)):
            if list1[i] != list2[j] and list2[j] != list3[k]:
                list3.append(1)
print(list3)

#for i in range(len(list1)):
#    for j in range(len(list1)):
#        if list1[i] != list1[j]:
#            list2.append(list1[j])
#print(list2)