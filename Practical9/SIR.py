import numpy as np
import matplotlib.pyplot as plt

N = 10000           
S0 = N - 1         
I0 = 1             
R0 = 0              

beta = 0.3         
gamma = 0.05       

S_list = [S0]
I_list = [I0]
R_list = [R0]

time_steps = 1000
for t in range(time_steps):
    S = S_list[-1]
    I = I_list[-1]
    R = R_list[-1]

    infection_prob = beta * (I / N)
    new_infections = np.random.binomial(S, infection_prob)
    new_recoveries = np.random.binomial(I, gamma)

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='red')
plt.plot(R_list, label='Recovered', color='green')
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR_model.png', dpi=150)   
plt.show()