# Question : https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-02

# My Solution :
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        output = [len(set(sorted_arr[:sorted_arr.index(i)]))+1  for i in arr]
        return output


# Verdict : 3 test cases failed
