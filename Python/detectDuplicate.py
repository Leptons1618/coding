# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         d = {}
#         for i in range(len(nums)):
#             if nums[i] in d.keys():
#                 return True
#             else: d[nums[i]] = 1
#         return False


# s = Solution()
# s.containsDuplicate(nums = [1, 2, 3, 1])
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = set()
        for i in nums:
            if i in d:
                return True
            else: d.add(i)
        return False
s = Solution()
print(s.containsDuplicate(nums=[2,14,18,22,22]))


