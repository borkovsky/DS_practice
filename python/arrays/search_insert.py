# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
	if target in nums:
		return nums.index(target)
	else:
		if target > nums[-1]:
			return(len(nums))
		elif target < nums[0]:
			return 0
		else:
			for i in range(len(nums)):
				if target > nums[i]:
					i += 1
				else:
					return i