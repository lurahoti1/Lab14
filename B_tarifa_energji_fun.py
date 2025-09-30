def tarifa_energji(kwh: int) -> int:
    if kwh < 0:
        return -1
    taksa = 120
    if kwh <= 100:
        total = kwh * 8
    elif kwh <= 300:
        total = kwh * 12
    else:
        total = kwh * 15
    return total + taksa

kwh = int(input("kWh: "))
totali = tarifa_energji(kwh)
if totali == -1:
    print("E pavlefshme")
else:
    print(f"Totali: {totali}")
