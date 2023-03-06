# Page 15 of Implementing Derivatives Models (Clewlow, Strickland, 1998)
# Implemented in Python 3.11 by Scott Griffin Jr., Univerity of Iowa, 2023

import math

def american_put(K,T,S,r,N,u,d):

    # precompute constants
    dt = T/N
    p = (math.exp(r*dt)-d)/(u-d)
    disc = math.exp(-r*dt)
    
    # inititalize asset prices at maturity (time N)
    St = [0]*(N+1)
    St[0] = S*(d**N)
    for i in range(1,N+1):
        St[i] = St[i-1]*(u/d)

    # initialize option payoffs at maturity
    C = [0]*(N+1)
    for i in range(0,N+1):
        C[i] = max(0,K-St[i])

    # step back through tree applying the early exercise condition
    for i in range(N,-1,-1):
        for j in range(0,i):
            C[j] = disc*(p*C[j+1] + (1-p)*C[j])
            St[j] = St[j]/d
            C[j] = max(C[j], K-St[j])

    return C[0]


# Textbook example
# K = 100
# S = 100
# T = 1
# N = 3
# r = 0.06
# u = 1.1
# d = 1/u
# print(american_put(K,T,S,r,N,u,d))



    
