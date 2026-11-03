import matplotlib.pyplot as plt
import csv

# Given data
y = [0, 2, 4, 6, 8, 10]
x = [3.00, 3.40, 3.20, 2.10, 1.10, 0.60]
h = y[1] - y[0]

# 1. Construct the forward difference table
table = [x[:]]
while len(table[-1]) > 1:
    previous = table[-1]
    current = []
    for i in range(len(previous) - 1):
        current.append(previous[i + 1] - previous[i])
    table.append(current)

print("Forward Difference Table:")
for row in table:
    print([round(value, 4) for value in row])

# 2. Newton's Forward Interpolation
def newton_forward(value):
    p = (value - y[0]) / h
    result = table[0][0]
    term = 1
    for i in range(1, len(table)):
        term = term * (p - i + 1) / i
        result = result + term * table[i][0]
    return result

# 3. Generate intermediate points for the left half
left_y = []
left_x = []
current = 0
while current <= 10:
    left_y.append(current)
    left_x.append(newton_forward(current))
    current = round(current + 0.1, 1)

# 4. Generate the right half using symmetry
right_x = [-value for value in left_x]

# 5. Find maximum half-width and its height
maximum_width = 0
maximum_height = 0
current = 0
while current <= 10:
    width = newton_forward(current)
    if width > maximum_width:
        maximum_width = width
        maximum_height = current

    current = round(current + 0.001, 3)
print("\nMaximum Half-Width:", round(maximum_width, 4), "cm")
print("Height at Maximum Width:", round(maximum_height, 4), "cm")

# 6. Find height where half-width is 2.00 cm
low = 6
high = 8
for i in range(50):
    mid = (low + high) / 2
    if newton_forward(mid) > 2:
        low = mid
    else:
        high = mid

height = (low + high) / 2
print("Height where Half-Width is 2.00 cm:",
      round(height, 4), "cm")

# 7. Export complete mirrored coordinates
with open("bottle_coordinates.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["X (cm)", "Y (cm)"])
    # Left half
    for i in range(len(left_y)):
        writer.writerow([round(-left_x[i], 4), round(left_y[i], 4)])
    # Right half
    for i in range(len(left_y) - 1, -1, -1):
        writer.writerow([round(left_x[i], 4), round(left_y[i], 4)])

print("\nComplete coordinates exported to bottle_coordinates.csv")

# 8. Plot the complete bottle silhouette
plt.plot([-value for value in left_x], left_y, label="Left Half")
plt.plot(left_x, left_y, label="Right Half")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.title("Reconstructed Bottle Silhouette")
plt.axvline(0, linestyle="--")
plt.grid()
plt.axis("equal")
plt.legend()
plt.show()