'''
Easy Level problem  : How to Convert Binary, back to decimal logic is enough
'''

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max = 0
        for i in permutations(nums,len(nums)):
            binary_numer = "".join(("".join(bin(i[0])).replace('0b',''),"".join(bin(i[1])).replace('0b',''),"".join(bin(i[2])).replace('0b','')))
            binary_equal = int(binary_numer,2)
            if binary_equal > max:
                max = binary_equal

        return max
