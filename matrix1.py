nums1 = []
nums2 = []
nums3 = []
nums4 = []
list1 = [nums1, nums2]
list2 = [nums3, nums4]
list3 = [[],[]]
num_count = int(input("How many numbers in each list? "))
for i in range(num_count):
    i = int(input("List 1: Enter a number: "))
    nums1.append(i)
for j in range(num_count):
    j = int(input("List 2: Enter a number: "))
    nums2.append(j)
for k in range(num_count):
    k = int(input("List 3: Enter a number: "))
    nums3.append(k)
for l in range(num_count):
    l = int(input("List 4: Enter a number: "))
    nums4.append(l)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        tot = list1[i][j] + list2[i][j]
        list3[i].append(tot)
print (list1)
print(list2)
print('=')
print(list3)




    