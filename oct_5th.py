class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)>2:
            sorted_skill = sorted(skill)

            # This is very poor approach , beats only 5% 
            '''
            pairs = []
            ans = 0
            for i in range(len(skill)):
                t1,t2 = sorted_skill[i],sorted_skill[len(skill)-1-i]
                pairs.append(tuple([t1,t2]))

            half = int(len(pairs)/2)
            pairs = pairs[:half] # duplicate pairs will be there , this is not needed
            
            '''

            # New Approach to find pairs cuttinng down looping 50%, this beats 23%
            pairs = [(sorted_skill[i], sorted_skill[~i]) for i in range(len(skill) // 2)]
            each_team_skill = sum(pairs[1])
            for i in pairs:
                if sum(i)!=each_team_skill:
                    ans = -1
                    break
                else:
                    ans+=i[0]*i[1]
        else:
            ans = (skill[0]*skill[1])

        return ans        
