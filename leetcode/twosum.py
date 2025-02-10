# nums = [2,7,11,15]
# target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6

# for i in range(0,len(nums)):
#     for j in range(0,len(nums)):
#         if i != j and i < j:
#             if nums[i] + nums[j] == target:
#                 print([i,j])
                
 



# a = {"nums" : [2,7,11,15], "target" : 9}
# b = {"nums" : [3,2,4], "target" : 6}
# c = {"nums" : [3,3], "target" : 6}

# class Solution:
#     # def __init__():
#     #     pass
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target



#     def twoSum(nums, target):
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums)):
#                 if i != j and i < j:
#                     if nums[i] + nums[j] == target:
#                         print([i,j])

# Solution.twoSum(a["nums"],a["target"])
# Solution.twoSum(b["nums"],b["target"])
# Solution.twoSum(c["nums"],c["target"])

   
class Solution(object):
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target


    def twoSum(self):
        for i in range(0,len(self.nums)):
            for j in range(0,len(self.nums)):
                if i != j and i < j:
                    if self.nums[i] + self.nums[j] == self.target:
                        return [i,j]

nums = [2,7,11,15]
target = 9
print(Solution(nums, target).twoSum())
