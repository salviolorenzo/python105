num_count = int(input("How many numbers would you like to add? "))
nums = []
counter = 0
while counter < num_count:
    user = int(input("Enter a number: "))
    nums.append(user)
    counter +=1

total = 0
for i in range(len(nums)):
    total += nums[i]
print (total)