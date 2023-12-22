def merge_sort(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    while i<len(left):
            result.append(left[i])
            i=i+1
    while j<len(right):
            result.append(right[j])
            j=j+1
    return result
def merge(l):
     if len(l)<2:
          return l[:]
     else:
          mid=len(l)//2
          left=merge(l[:mid])
          right=merge(l[mid:])
          return merge_sort(left,right)
l1=[45,5,56,43,67,8,6]
print(merge(l1))

    