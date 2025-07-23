import random
# def sorting(list):
#         for j in range(len(list)-1):
#             for i in range(len(list)-1):
#                 if list[i]>list[i+1]:
#                     thingie=list[i]
#                     thingie2=list[i+1]
#                     list[i]=thingie2
#                     list[i+1]=thingie
#         return list


# listss=[4, 67, 12, 93, 2, 55, 81, 17, 3, 76, 20, 99, 8, 42, 5, 61, 100, 28, 7, 33, 19, 50, 90, 1, 45, 15, 88, 24, 72, 39, 6, 58, 95, 11, 30, 85, 21, 69, 14, 47, 78, 36, 92, 52, 10, 80, 27, 64, 41, 18, 75, 32, 97, 59, 13, 49, 23, 66, 83, 9, 71, 37, 54, 16, 29, 62, 96, 43, 79, 34, 57, 18, 25, 68, 89, 94, 46, 73, 31, 51, 100, 22, 65, 40, 70, 35, 56, 82, 98, 26, 63, 44, 87, 77, 38, 53, 100]
# print(sorting(listss))

# ---------------------------------------------------------

# def sorts(list):
#     for i in range(len(list)):
#         smallnum=smallestnum(i,list)
#         list[i], list[smallnum] = list[smallnum], list[i]
#     return list

# def smallestnum(line,list):
#     x=line
#     for i in range(line+1,len(list),1):
#         if list[i]<list[x]:
#             x=i
#     return x

# lists=[7,2,9,1,6]
# print(sorts(lists))

# ------------------------------------------------------

# def sorting(array1,array2):
#     x=0
#     y=0
#     output=[]
#     length = max(len(array1), len(array2))
#     for i in range(length):
#         if array1[y]>array2[x]:
#             output.append(array2[x])
#             x+=1
#             if x >= len(array2):
#                 for j in range(y,len(array1)):
#                     output.append(array1[j])
#                 return output
#         else:
#             output.append(array1[y])
#             y=y+1
#             if y >= len(array1):
#                 for j in range(x,len(array2)):
#                     output.append(array2[j])
#                 return output
#     return output
# def mergesort(list):
#     if len(list)<=1:
#         return list
#     list1=list[0:len(list)//2]
#     list2=list[len(list)//2:len(list)]
#     list1=mergesort(list1)
#     list2=mergesort(list2)
#     return sorting(list1,list2)
# print(mergesort([2,4,6,1,3,5,7,9,11]))

# ---------------------------------------------------

# def sort(list):
    # pivot=0
    # smalllist=[]
    # pivotlist=[]
    # biglist=[]
    # if len(list) <= 1:
    #     return list
    # else:
    #     for i in range(len(list)):
    #         if list[i] < list[pivot]:
    #             smalllist.append(list[i])
    #             smalllist = sort(smalllist)
    #         if list[i] == list[pivot]:
    #             pivotlist.append(list[pivot])
    #         if list[i] > list[pivot]:
    #             biglist.append(list[i])
    #             biglist = sort(biglist)
    #     return smalllist+pivotlist+biglist



def partition(list,l,r):
    pivot=list[r]
    hehe=l-1
    for j in range(l,r):
        if list[j]<=pivot:
            hehe+=1
            list[hehe],list[j] = list[j],list[hehe]
    list[hehe+1], list[r] = list[r], list[hehe+1]
    return hehe+1

def quicksort(list,l,r):
    if l<r:
        pivot=partition(list,l,r)
        quicksort(list,l,pivot-1)
        quicksort(list,pivot+1,r)

listt = []
# for i in range(10,0,-1):
#     soyeah=int(input("Pick " + str(i) + " unscrambled numbers: "))
#     listt.append(soyeah)
for i in range(1000):
    listt.append(random.randint(1, 10000))

#quicksort(listt, 0, len(listt) - 1)
print(listt)