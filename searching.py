list=[1,3,5,7,9,11,13,15,20,21,253,266,712,892]
# def find(num):
#     for i in range(len(list)):
#         if list[i]==num:
#             return i

# print(find(21)+1)

def search(start,end,target,list):
    
    mid=round((start+end)/2)
    
    if list[mid]==target:
        return mid +1
    elif list[mid]<target:
        start=mid+1
        mid=round((start+end)/2)
    elif list[mid]>target:
        end=mid-1
        mid=round((start+end)/2)
    return search(start,end,target,list)
    
print(search(0,13,712,list))
