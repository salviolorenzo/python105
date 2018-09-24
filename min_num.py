nums=[]
num_count = int(input("How many numbers? "))
for i in range(num_count):
    num_in = int(input("Enter a number: "))
    nums.append(num_in)
min_num = min(nums)
print("The smallest number is %d" %min_num)