# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

def findMedianSortedArrays(nums1, nums2):
	res = sorted(nums1+nums2)
	lenght = len(res)
	if len(res) % 2 == 0:
		return (res[lenght//2-1]+res[lenght//2])/2
	else:
		return res[lenght//2]

