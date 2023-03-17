number = input("Enter some nuber")
x = ""
z = 0

for i in range(0, 3):
    x += number
    z += int(x)

print(z)

a1 = "%s" % number
a2 = "%s%s" % (number, number)
a3 = "%s%s%s" % (number, number, number)
res = int(a1) + int(a2) + int(a3)
print(res)
