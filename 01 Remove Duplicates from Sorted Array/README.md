# Description of the topic
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

**Example 1:**

>
>Given nums = [1,1,2],
>
>Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
>
>It doesn't matter what you leave beyond the returned length.


**Example 2:**

>
>Given nums = [0,0,1,1,1,2,2,3,3,4],
>
>Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
>
>It doesn't matter what values are set beyond the returned length.

# Problem solving
前后一一进行比较，如果发现不同的，则将那个位置留住。否则不予理会。
# Code
```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        newTail = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1
```
# Error-prone point
直接对原数组进行操作。
输出数组的长度，超过输出数组的长度的都可以不用考虑。不是说要新开一个数组，输出一个完全没有重复项的数组。
return的时候返回的是实际的长度，所以返回的时候还要+1。
