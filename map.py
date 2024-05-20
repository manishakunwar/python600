nums = [8, 2, 1, 3, 5, 6]
#square each number
# sq = []
# index = 0

# while index < len(nums):   # for index in range(len(nums)):
#     item = nums[index]
#     sq.append(item**2)
#     index = index + 1
# print(f"Square is {sq}")



sq = list( map(lambda x : x**2, nums))
print(sq)



