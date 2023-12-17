tup=((2,"hello"),(4,"yellow"),(5,"dello"))
nums=()
words=()
for j in tup:
    nums=nums+(j[0],)
    if j[1].lower() not in words:
        words=words+(j[1].lower(),)
unique_words=len(words)
print(max(nums),min(nums),unique_words)
