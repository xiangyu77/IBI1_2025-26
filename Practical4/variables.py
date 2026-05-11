# Population change calculation
a = 5.08  # Scotland population in 2004 (millions)
b = 5.33  # 2014
c = 5.55  # 2024

d = b - a  # Change 2004–2014
e = c - b  # Change 2014–2024

print("Population change 2004–2014:", d, "million")
print("Population change 2014–2024:", e, "million")

if d > e:
    print("Population growth is decelerating.")
elif d < e:
    print("Population growth is accelerating.")
else:
    print("Population growth is stable.")

# Boolean logic
X = True
Y = False
W = X or Y
print("\nTruth table for OR:")
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)
