# Page 22 of Implementing Derivatives Models (Clewlow, Strickland, 1998)
# Implemented in Python3 by Scott Griffin Jr., Univerity of Iowa, 2023

import math

def general_additive_binomial_valuation_euro_call(K,T,S,sig,r,N):
    
    # set coefficients
    dt = T/N
    nu = r - 0.5*sig**2
    dxu = math.sqrt(sig**2*dt + (nu*dt)**2)
    dxd = -dxu
    pu = 0.5 + 0.5*(nu*dt/dxu)
    pd = 1-pu

    # precompute constants
    disc = math.exp(-r*dt)

    # initialize asset prices at maturity N
    St = [0]*(N+1)
    St[0] = S*math.exp(N*dxd)
    for i in range(1,N+1):
        St[i] = St[i-1]*math.exp(dxu-dxd)
    
    # initialize option values at maturity
    C = [0]*(N+1)
    for i in range(0,N+1):
        C[i] = max(0,St[i]-K)
    
    # step back through the tree
    for i in range(N,-1,-1):
        for j in range(0,i):
            C[j] = disc*(pu*C[j+1] + pd*C[j])

    return C[0]


# Textbook example
# K = 100
# T = 1
# S = 100
# sig = 0.2
# r = 0.06
# N = 3
# print(general_additive_binomial_valuation_euro_call(K,T,S,sig,r,N))
