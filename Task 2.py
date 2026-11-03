# Given data
T = [20, 45, 70, 100, 140]
V = [0.79, 1.82, 2.86, 4.12, 5.79]

# 1. Aitken's Interpolation
def aitken(x, y, value):
    p = y[:]
    n = len(x)
    for j in range(1, n):
        for i in range(n - j):
            p[i] = (
                (value - x[i + j]) * p[i]
                + (x[i] - value) * p[i + 1]
            ) / (x[i] - x[i + j])
    return p[0]

# 2. Lagrange Interpolation
def lagrange(x, y, value):
    result = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term = term * (value - x[j]) / (x[i] - x[j])

        result = result + term
    return result

# 3. Temperature to Voltage
print("--- Temperature to Voltage ---")
for temp in [55, 125]:
    a = aitken(T, V, temp)
    l = lagrange(T, V, temp)

    print("\nTemperature:", temp, "C")
    print("Aitken Voltage:", round(a, 4), "mV")
    print("Lagrange Voltage:", round(l, 4), "mV")
    print("Difference:", round(abs(a - l), 4))

# 4. Voltage to Temperature (Inverse Interpolation)
print("\n--- Voltage to Temperature ---")

for voltage in [3.50, 5.00]:
    a = aitken(V, T, voltage)
    l = lagrange(V, T, voltage)

    print("\nVoltage:", voltage, "mV")
    print("Aitken Temperature:", round(a, 4), "C")
    print("Lagrange Temperature:", round(l, 4), "C")
    print("Difference:", round(abs(a - l), 4))

# 5. Summary
print("\n--- Summary ---")
print("Methods: Aitken and Lagrange")
print("Polynomial degree: 4")
print("Data spacing: Unequal")