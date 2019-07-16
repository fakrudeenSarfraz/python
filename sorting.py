lst = [10,2,17,19,9]
val = len(lst)
j = 1

for i in range(val):
    for j in range(val):
        if lst[i] < lst[j] :
            temp = lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
            
            
