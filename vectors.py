nums1 = []
nums2 = []
num_totals = []
num_count = int(input("How many numbers in each list? "))
for i in range(num_count):
    i = int(input("List 1: Enter a number: "))
    nums1.append(i)
for j in range(num_count):
    j = int(input("List 2: Enter a number: "))
    nums2.append(j)
for k in range(len(nums1)):
    total = nums1[k]*nums2[k]
    num_totals.append(total)
print(num_totals)