# def union(nums1,nums2):
#     i=0
#     j=0
#     union=[]
#     print(len(union))
#     while (i<len(nums1) and j<len(nums2)):
#         if (nums1[i]<nums2[j]):
#          if(len(union)==0):
#              union.append(nums1[i])
#              i=i+1
#          elif( union[-1]!=nums1[i] ):
#              union.append(nums1[i])
#              i=i+1
#     while(i<len(nums1)):
#          if(union[-1]!=nums1[i]):
#              union.append(nums1[i])
#              i=i+1
#     while(j<len(nums1)):
#          if(union[-1]!=nums1[j]):
#              union.append(nums1[j])
#              j=j+1         
#     return union    


def inter(l1,l2):
    i=0
    j=0
    intersect =[]
    while(i<len(l1) and j<len(l2)):
        if(l1[i]>l2[j]):
            j=j+1
        elif(l1[i]<l2[j]):
            i=i+1
        else:
            intersect.append(l1[i])
            i=i+1
            j=j+1
    return intersect    

l1=[1,2,3,3,4,5,6]     
l2=[2,3,3,5,6,6,7]     
print(inter(l1,l2))        
            
            
            
# def inter(l1,l2):
#     i=0
#     j=0
#     intersect = []
#     while(i<len(l1) and j<len(l2)):
#         if(l1[i]>l2[j]):
#             j=j+1
#         elif(l1[i]<l2[j]):
#             i=i+1
#         else:
#              intersect.append(l1[i])
#              i=i+1
#              j=j+1
#     return intersect    

# l1=[1,2,3,3,4,5,6]     
# l2=[2,3,3,5,6,6,7]     
# print(inter(l1,l2),"hi")           
        
        
        
        
        
# nums1=[1,1,2,3,3,5,6,7,7]        
# nums2=[3,5,4,4,9,10,11]
# print(union(nums1,nums2))
        