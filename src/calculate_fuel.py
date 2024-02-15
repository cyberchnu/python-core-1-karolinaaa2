def calculate_fuel(distance):
  # Type your code
  # Перевірка, чи введена вірна відстань
  if not isinstance(distance, (int, float)) or distance <= 0:
    print(" відстань (10)")
    return None

  # Розрахунок обсягу палива (при умові, що потрібно 10 разів більше палива, ніж відстань)
  fuel_amount = distance * 10

  # Перевірка, щоб обсяг палива був не менше 100 літрів
  if fuel_amount < 100:
    return 100
  else:
    return fuel_amount

  # Приклад виклику функції


distance = 20
result = calculate_fuel(distance)
print(result)