nums= []
num_count = int(input("How many numbers? "))
for i in range(num_count):
    i = int(input("Enter a number: "))
    nums.append(i)
for j in range(len(nums)):
    if nums[j] > 0:
        print(nums[j])