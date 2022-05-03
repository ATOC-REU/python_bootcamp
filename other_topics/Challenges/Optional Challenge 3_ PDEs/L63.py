import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#The differential equation system using 3 parameters
def lorenz_63(state_vector, t, sigma, beta, rho):  
    u, v, w = state_vector
    u_next = sigma*(v-u)
    v_next = u*(rho-w)-v
    w_next = u*v - beta*w
    return u_next, v_next, w_next

#The function to create results of a Lorenz 63 system.
def run_l63(initial_conditions, total_time, number_of_steps):
    if(len(initial_conditions)!=3):
        print("Make sure the initial conditions are (3,1) array of floats")
        return
        
    t = np.linspace(0,total_time, number_of_steps)
    sigma = 10
    beta = 8.0/3.0
    rho = 28

    sol = odeint(lorenz_63, initial_conditions, t, args=(sigma, beta, rho))

    return sol

#The function to plot L63 data to be used in conjunction with run_l63
def plot_l63(data):
    fig = plt.figure(figsize=(12,8))
    ax = fig.gca(projection='3d')
    ax.plot(data[:,0], data[:,1], data[:,2])
    plt.show()