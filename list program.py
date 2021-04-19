# Empty list:
my_list = []
# Enter how many name's
a = int(input("How many name\'s you want: "))

for i in range(a):
  i = str(input("Enter the name: "))
  my_list.append(i)

print("Your name list", my_list)
