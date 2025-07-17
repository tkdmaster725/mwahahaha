def fs(x):
    if x==1:
        return 1
    if x==2:
        return 1
    return (fs(x-1)+fs(x-2))
print(fs(12))
