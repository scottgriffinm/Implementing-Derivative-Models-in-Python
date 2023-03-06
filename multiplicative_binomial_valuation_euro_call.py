# Page 13 of Implementing Derivatives Models (Clewlow, Strickland, 1998)
# Implemented in Python3 by Scott Griffin Jr., University of Iowa, 2023

import math

def multiplicative_binomial_valuation_euro_call(K,T,S,r,N, u, d):
    # set coefficients
    dt = T/N
    p = (math.exp(r*dt)-d)/(u-d)
    disc = math.exp(-r*dt)

    # initialize asset prices at maturity N
    St = [0]*(N+1)
    St[0] = S*(d**N)
    for i in range(1,N+1):
        St[i] = St[i-1]*u/d

    # initialize option values at maturity
    C = [0]*(N+1)
    for i in range(0,N+1):
        C[i] = max(0,St[i]-K)

    # step back through the tree
    for i in range(N,-1,-1):
        for j in range(0,i):
            C[j] = disc*(p*C[j+1] + (1-p)*C[j])

    return C[0]


# Textbook example
# K = 100
# T = 1
# S = 100
# r = 0.06
# N = 3
# u = 1.1
# d = 1/u
# print(multiplicative_binomial_valuation_euro_call(K,T,S,r,N,u,d))