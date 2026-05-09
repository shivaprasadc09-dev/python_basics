"""
Allow only audience above age 18
"""
try:
    age = input("enter the age of the audience: ")
    if age > 18:
        print(f"Audience age is {age} hence he/she is allowed inside" )
    else:
        print("Audience is not allowed inside")

except Exception:
    print("Age must be a number")