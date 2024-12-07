# SIR Model - Detrministic

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
beta = 0.3  #Transmission rate
gamma = 0.1 #Recovery rate

#Initial conditions
S0 = 0.99 # Initial susceptible population
I0 = 0.01 # Initial infected population
R0 = 0.0  # Initial recovered population
initial_conditions = [S0, I0, R0]

# Time vector (in days)
t = np.linspace(0, 160, 160)

# SIR model differential equations
def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I -gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Integrate the SIR equations
solution = odeint(sir_model, initial_conditions, t, args=(beta, gamma))
S, I, R = solution.T

#Plot results
plt.figure(figsize = (10, 6))
plt.plot(t, S,'b', label='Susceptible')
plt.plot(t, I, 'r',label= 'Infected')
plt.plot(t, R, 'g',label = 'Recovered')
plt.xlabel('Time(days)')
plt.ylabel('Proportion of population')
plt.legend()
plt.title('SIR Model - Deterministic')
plt.savefig('SIR_model_deterministic')
plt.show()



