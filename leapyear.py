val = int(input("Enter the value :"))

if(val%4==0 and val%100 != 0 or val%400==0 ):
    print("it's a leapyear")
else:
    print("it is not a leapyear")
