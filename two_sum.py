#T.C. O(n)
#S.C. O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Hashmap solution
        prevMap = {} # will only add val:index after iterating through the array
        #using enumerate here as it will give the index i and value n
        for i,n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        

        #Bruteforce solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
