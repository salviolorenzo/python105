nums=[]
num_count = int(input("How many numbers? "))
counter = 0
while counter< num_count:
    num_in = int(input("Enter a number: "))
    nums.append(num_in)
    counter += 1
max_num = max(nums)
print("The largest number is %d" %max_num)