
from decimal import Decimal
possibility = [0, 0, 0, 0.1, 0.25, 0.35, 0.4, 0.65, 0.85, 0.95, 1]
# possibility = [0, 0, 0,0,0,0,0,0,0,0,0, 0.2, 0.45, 0.7, 0.8, 0.95, 1]

theta = 7

for i in range(len(possibility)):
    expect = theta * Decimal(str(possibility[i]))
    print("index" + str(i))
    for j in range(i):
        expect = expect - j*(Decimal(str(possibility[j+1]))-Decimal(str(possibility[j])))

    print(expect)

