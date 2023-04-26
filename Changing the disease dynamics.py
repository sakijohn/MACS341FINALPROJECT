import matplotlib.pyplot as plt
import numpy as np

# define model parameters
beta = 0.3
gamma = 0.1
R0 = beta/gamma
N = 100000
I0 = 1
S0 = N - I0
R0 = 1e-8  # add small constant to avoid division by zero error
S1 = int(N*0.9)

# define function to calculate SIR model
def SIR_model(S, I, R, beta, gamma):
    dSdt = -beta*S*I/N
    dIdt = beta*S*I/N - gamma*I
    dRdt = gamma*I
    return dSdt, dIdt, dRdt

# define function to simulate SIR model
def simulate_SIR_model(S0, I0, R0, beta, gamma, days):
    S = [S0]
    I = [I0]
    R = [R0]
    for day in range(days):
        dSdt, dIdt, dRdt = SIR_model(S[-1], I[-1], R[-1], beta, gamma)
        S.append(S[-1]+dSdt)
        I.append(I[-1]+dIdt)
        R.append(R[-1]+dRdt)
    return np.array(S), np.array(I), np.array(R)

# simulate SIR model with different strategies
S1_1, I1_1, R1_1 = simulate_SIR_model(S0, I0, R0, 0.25, gamma, 365)
S1_2, I1_2, R1_2 = simulate_SIR_model(S0, I0, R0, beta, 0.125, 365)
S1_3, I1_3, R1_3 = simulate_SIR_model(S1, I0, R0, beta, gamma, 365)

# plot results
fig, ax = plt.subplots(1, 2, figsize=(12,6))
fig.suptitle('Impact of different strategies on COVID-19 dynamics', fontsize=16)
ax[0].plot(I1_1/N, label='Strategy 1')
ax[0].plot(I1_2/N, label='Strategy 2')
ax[0].plot(I1_3/N, label='Strategy 3')
ax[0].set(title='Percentage of population that is infectious', xlabel='Days', ylabel='Percentage')
ax[0].legend()
ax[1].plot(np.cumsum(I1_1)/N*10, label='Strategy 1')
ax[1].plot(np.cumsum(I1_2)/N*10, label='Strategy 2')
ax[1].plot(np.cumsum(I1_3)/N*10, label='Strategy 3')
ax[1].set(title='Cumulative percentage of population infected', xlabel='Days', ylabel='Percentage')
ax[1].legend()
plt.show()

