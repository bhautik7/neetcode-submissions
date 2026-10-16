class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodOfArray=1
        hasZero=0
        for num in nums:
            if num==0:
                hasZero+=1
                continue
            prodOfArray*=num
        
        ans=[]
        
        if hasZero==1:
            for num in nums:
                if num==0:
                    ans.append(prodOfArray)
                else:
                    ans.append(0)
        elif hasZero>1:
            ans=[0]*len(nums)
        else:
            for num in nums:
                ans.append(prodOfArray//num)
        
        return ans