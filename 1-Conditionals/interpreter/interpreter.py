# x is an int, y is math symbols, z is also int

math = input("arithmetic expression: ")
x, y, z = math.split(" ")

x = float(x)
z = float(z)

if y == "+":
    ans = print((x) + (z))

print(ans)
