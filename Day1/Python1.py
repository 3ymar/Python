import datetime

now = datetime.datetime.now()
currentyear = now.year

birth = int(input("Enter year of Birth:"))

age = currentyear-birth

if age < 18:
    print("You are a minor.")
    
elif age > 18 and age <36:
    print("You are a youth.")
    
else:
    print("You are  an elder.")



    