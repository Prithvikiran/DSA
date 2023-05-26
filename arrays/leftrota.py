
# def leftrotate_oneplace(nums, n):
#     temp=nums[0]
#     for i  in range(len(nums)-1):
#         nums[i]=nums[i+1]   
#     nums[len(nums)-1]=temp
#     return nums

# nums=[1,2,3,4,5,6,7,8]

# print(leftrotate_oneplace(nums,1))

# def leftrotateby_dplaces(nums,d):
#     temp=[]
#     for i in range(d):
#         temp.append(nums[i])
#     for j in range(len(nums)-d):
#         nums[j]=nums[j+d]  
#     for i in range(d+1,len(nums)-1):
#         nums[i]=temp[i-d]
#     return nums




# nums=[1,2,3,4,5,6,7]
# print(leftrotateby_dplaces(nums,3))
        
        
           
        
    