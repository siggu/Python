B = int(input())

atmospheric_pressure = 5 * B - 400

print(atmospheric_pressure)
if atmospheric_pressure < 100:
    print(1)
elif atmospheric_pressure > 100:
    print(-1)
else:
    print(0)