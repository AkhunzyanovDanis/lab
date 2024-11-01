salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
expenses = 0
earnings = 0
for _ in range(months):
    earnings = earnings + salary
    expenses = expenses + spend
    spend = spend * (increase + 1)
m = expenses - earnings
import math
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(m))
