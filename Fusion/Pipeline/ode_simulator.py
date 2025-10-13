# ode_simulator.py
import numpy as np
import networkx as nx
from scipy.integrate import solve_ivp

def simulate_graph(G, params, t_eval):
    n = len(G.nodes)
    A = nx.adjacency_matrix(G).astype(float)
    L = nx.laplacian_matrix(G).astype(float)
    beta, gamma, p, rp, delta, rd, c, D_V = (
        params['beta'], params['gamma'], params['p'],
        params['rp'], params['delta'], params['rd'],
        params['c'], params['D_V']
    )

    # initial conditions
    T0 = np.ones(n)
    I0 = np.zeros(n)
    S0 = np.zeros(n)
    V0 = np.zeros(n)
    V0[np.random.randint(0, n, 5)] = 1e4  # random initial infection
    y0 = np.concatenate([T0, I0, S0, V0])

    def rhs(t, y):
        T, I, S, V = np.split(y, 4)
        dT = -beta * T * V - gamma * T * (A @ I)
        dI = beta * T * V - gamma * I * (A @ T) - delta * I
        dS = gamma * T * (A @ I) - rd * delta * S
        dV = p * I + rp * p * S - c * V + D_V * L @ V
        return np.concatenate([dT, dI, dS, dV])

    sol = solve_ivp(rhs, (t_eval[0], t_eval[-1]), y0, t_eval=t_eval, rtol=1e-5)
    return sol
