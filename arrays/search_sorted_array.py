# search in sorted array consist of integer where every element appears
# exactly twice, except one find that non repeating element

def search_sorted_array(nums,n):
    n = len(nums)
    l,r = 0,n-1
    while l<=r:
        mid = (l+r)//2
        if mid == l:
            return nums[mid]
        elif mid%2 == 0:
            if nums[mid] == nums[mid+1]:
                l = mid+2
            elif nums[mid] == nums[mid-1]:
                r = mid-2
            else:
                return nums[mid]
        else:
            if nums[mid] == nums[mid-1]:
                l = mid+1
            elif nums[mid] == nums[mid+1]:
                r = mid-1
            else:
                return nums[mid]
    return -1

nums = [1,1,2,2,3,3,4,4,8]
print(search_sorted_array(nums,len(nums)))