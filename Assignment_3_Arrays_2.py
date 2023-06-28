def fourSum(nums,target: int):
    n=len(nums)
    nums.sort()
    ans=[]
    i=0
    while i<n:
        j=i+1
        while j<n:
            end=n-1
            strt=j+1
            nTarget=target-nums[i]-nums[j]
            
            while strt<end:                    
                if nums[strt]+nums[end]==nTarget:
                    ans.append([nums[i],nums[j],nums[strt],nums[end]])

                    third=nums[strt]
                    fourth=nums[end]
                    while strt<end and nums[strt]==third:
                        strt+=1
                    while strt<end and nums[end]==fourth:
                        end-=1
                elif nums[strt]+nums[end]>nTarget:
                    end-=1
                else:
                    strt+=1
            t=nums[j]
            while j<n and nums[j]==t:
                j+=1
        t2=nums[i]
        while i<n and nums[i]==t2:
            i+=1
    return ans


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(fourSum(nums,target))