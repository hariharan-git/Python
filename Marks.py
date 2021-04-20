# Enter the marks:
a = int(input("Enter the science marks: "))
b = int(input("Enter the english marks: "))
c = int(input("Enter the tamil marks: "))
d = int(input("Enter the social science marks: "))
e = int(input("Enter the maths marks: "))

print()
print("-----------Mark sheet-----------")

if a <= 39:
    print("Fail in science")
elif b <= 39:
    print("Fail in english")
elif c <= 39:
    print("Fail in tamil")
elif d <= 39:
    print("Fail in social science")
elif e <= 39:
    print("Fail in maths")

x = (a+b+c+d+e)
print("The total marks: ", x)
