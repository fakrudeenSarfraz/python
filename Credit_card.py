import re
count = 0
credit=input("Enter your credit card number")
match=re.search(r'[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',credit)
if(match):
    if(credit[4]=='-'):
        credit=credit.replace('-','')
    l=len(credit)
    for i in range(0,l-1,1):
        if credit[i]==credit[i+1]:
            count+=1
            if(count >= 4):
                print("invalid")
                break
        else:
            count = 0
    if(count < 4):
        print("valid")
else:
    print("Invalid")
