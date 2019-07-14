import re

strval=input("Enter the string : ")

match=re.sub('[^&]&&[^&]',' and ',strval)

strval=re.sub('[^\|]\|\|[^\|]',' or ',match)

print(strval)
