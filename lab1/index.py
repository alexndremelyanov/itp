HEIGHT = 173
WEIGHT = 65
STEPS = 8000
TIME = 20

length = HEIGHT / 4 + 0.37
distance = length * STEPS
speed = length / TIME
expense = 0.035 * WEIGHT + ((speed ** 2) / HEIGHT) * 0.029 * WEIGHT

print(f'Distance is: {length} m, Expense is: {expense} kcal/min')
print(f'Distance is: {length / 1000} km, Expense is: {expense} kcal/min')

if length < 2000:
    print('Error: distance too small')
elif length < 4000:
    print('Normal distance')
else:
    print('Distance too large')
