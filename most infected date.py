import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
beta = 0.3
gamma = 0.1
population = 10000000
days = 151 # 0 to 150 days

# Initial infection rates from 0.001% to 10%
initial_infection_rates = np.linspace(0.001, 1, 1000)
most_infected_days = []  # To store the day with most infected cases
infected_per_day = []  # To store infected cases per day

# Loop through initial infection rates
for i, initial_infected_rate in enumerate(initial_infection_rates):
    initial_infected = int(initial_infected_rate * population)
    # Run SIR simulation
    S = [population - initial_infected]
    I = [initial_infected]
    R = [0]
    most_infected = 0
    for t in range(1, days):
        dS = -beta * S[-1] * I[-1] / population
        dI = beta * S[-1] * I[-1] / population - gamma * I[-1]
        dR = gamma * I[-1]
        S.append(S[-1] + dS)
        I.append(I[-1] + dI)
        R.append(R[-1] + dR)
        # Update most infected day
        if I[-1] > most_infected:
            most_infected = I[-1]
            most_infected_day = t
    most_infected_days.append(most_infected_day)
    infected_per_day.append(I)

# Create DataFrame
df = pd.DataFrame({'Initial Infected Rate': initial_infection_rates,
                   'Most Infected Day': most_infected_days,
                   'Infected Cases Per Day': infected_per_day})

# Export to Excel
df.to_excel('sir_simulation_results.xlsx', index=False)

# Plot the most infected day
plt.plot(initial_infection_rates, most_infected_days)
plt.xlabel('Initial Infected Rate (%)')
plt.ylabel('Most Infected Day')
plt.title('Most Infected Day vs. Initial Infected Rate')
plt.show()
