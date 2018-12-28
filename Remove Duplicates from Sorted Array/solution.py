def removeDuplicates(nums):
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

nums = [1,1,1,2]
removeDuplicates(nums)
print (nums)