nums = []
num_count = int(input("How many numbers? "))
for i in range(num_count):
    user_num = int(input("Enter a number: "))
    nums.append(user_num)
for j in range(len(nums)):
    if nums[j]%2 == 0:
        print(nums[j],end=', ')
print()

