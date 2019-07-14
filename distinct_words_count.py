n=int(input("Enter the nummber : "))
word=[]
count=[]
for i in range(n):
    word.append(input())
    
for i in range(len(word)):
    count.append(1)
    for j in range(len(word)):
        if word[i] == word[j] :
            if i<j:
                count[i]+=1
            elif i>j:
                count[i]=0
                break
print(count)
for i in count:
    if i!=0:
        print(i, end=' ')
    
