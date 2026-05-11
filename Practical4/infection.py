# Pseudo-code:
# 1. Set initial infected, growth rate, total population
# 2. Initialize day counter = 0
# 3. While infected < total:
#    - Increase day
#    - Calculate new infections
#    - Update infected count
#    - Print daily status
# 4. Print total days taken

initial_infected = 5
growth_rate = 0.4
total_population = 91

infected = initial_infected
days = 0

print("Day 0: infected =", infected)

while infected < total_population:
    days += 1
    new_infections = infected * growth_rate
    infected = infected + new_infections
    print(f"Day {days}: infected = {infected:.0f}")

print(f"\nIt took {days} days to infect all {total_population} students.")