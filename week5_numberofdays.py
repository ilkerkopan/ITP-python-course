# number of days in month
print("enter months number")
month=input()

if month=="1" or month=="3" or month=="5" or month=="7" or month=="8" or month=="10" or month=="12":
    print("number of days 31")
elif month=="2":
    print("number of days 28")
elif month=="4" or month=="6" or month=="9" or month=="11":
    print("number of days 30")