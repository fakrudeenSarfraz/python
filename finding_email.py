import re

val = int(input("Enter the total email address :"))
lst = []
lst2 = []
for i in range(val):
    lst.append(input())

for i in range(val):
    match = re.search(r'[a-zA-Z0-9\-]+@[a-zA-Z0-9]+.[a-zA-Z]+',lst[i])
    if match:
        lst2.append(lst[i])
    print(match)
print(lst2)
