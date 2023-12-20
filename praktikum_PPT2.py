def lengthOfLIS(nums):    
    n = len(nums)
    ans = []
         
    ans.append(nums[0])
 
    for i in range(1, n):
        if nums[i] > ans[-1]:                                                                        
            ans.append(nums[i])
        else:                                                                                    
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid                                                
            ans[low] = nums[i]
             
    return len(ans)
 
if __name__ == "__main__":
    nums = [4, 1, 13, 7, 0, 2, 8, 11, 3]    
    print("Length of LIS is", lengthOfLIS(nums))