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

def sorts(list):
    for i in range(len(list)):
        smallnum=smallestnum(i,list)
        list[i], list[smallnum] = list[smallnum], list[i]
    return list

def smallestnum(line,list):
    x=line
    for i in range(line+1,len(list),1):
        if list[i]<list[x]:
            x=i
    return x

lists=[7,2,9,1,6]
print(sorts(lists))
