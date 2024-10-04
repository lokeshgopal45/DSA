class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
      pairs = [(arr[i], arr[~i]) for i in range(len(arr) // 2)]
      ans = sum([1 for i in pairs if sum(i)%k==0])
      return (len(pairs)==ans)
        
