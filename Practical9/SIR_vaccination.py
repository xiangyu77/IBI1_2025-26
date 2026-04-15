import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(8, 5), dpi=150)

for v in vaccination_rates:
    vaccinated = int(N * v)
    S = N - vaccinated - 1
    I = 1
    R = vaccinated

    S_list = [S]
    I_list = [I]
    R_list = [R]

    for t in range(time_steps):
        infection_prob = beta * (I / N)

        if S > 0:
            new_infections = np.random.binomial(S, infection_prob)
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.random.binomial(I, gamma)
        else:
            new_recoveries = 0

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        if S < 0:
            S = 0
        if I < 0:
            I = 0

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    plt.plot(I_list, label=f'Vaccination {int(v*100)}%')

plt.xlabel('Time step')
plt.ylabel('Number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig('SIR_vaccination.png', dpi=150)
plt.show()