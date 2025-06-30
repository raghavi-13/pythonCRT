
name=input("Enter your name : ")
a=(f"Hello {name}")
print(a)
age=int(input("Enter your age : "))
if age>18:
    print(f"You are Eligible for voting {name}.")
elif age==18:
    pritn("Welcome new voter {name}.")
else :
    print("You are not Eligible {name}.")