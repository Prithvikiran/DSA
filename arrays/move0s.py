
# def moveZeroes(nums) -> None:
#        l1=[]
#        l2=[]

#        for i in range(len(nums)):

#         if nums[i]==0:
#             l1.append(nums[i])
#         else:
#             l2.append(nums[i])
        
#        for i in range(len(l1)):
#          l2.append(l1[i])

#        for i in range(len(l2)):

#           nums[i]=l2[i]
          
          
# nums=[2,34,0,7,0]                   
# moveZeroes(nums)  
                  
# print(nums)    



# def moveopt(nums):
#     j=-1
#     for i in range(len(nums)):
#      if nums[i]==0:
#          j=i
#          break
#      for i in range(j+1,len(nums)):
#         if (nums[i]!=0):
#            nums[i],nums[j]=nums[j],nums[i]
#            j=j+1

        
              
# nums=[2,34,0,7,0]                   
# moveopt(nums)  
                  
# print(nums) 


