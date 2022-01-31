#logical operator
citizen=input("Enter citizenship:").lower()
age=int(input("Enter age:"))
if(citizen=="kenyan" and age>=18):
    print("Vote")
else:
    print("Disqualified")

