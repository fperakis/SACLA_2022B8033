import numpy as np

# ----------------------------- modified atomic form factors (MAFF)
def maffO(alphaO, delta, q):
    # Waasmaier/Kirfel five gaussian coefficients
    a1 = 2.960427
    a2 = 2.508818
    a3 = 0.637853
    a4 = 0.722838
    a5 = 1.142756
    b1 = 14.182259
    b2 = 5.936858
    b3 = 0.112726
    b4 = 34.958481
    b5 = 0.390240
    c  = 0.027014
    
    affO = a1*np.exp(-b1*(q**2)) + a2*np.exp(-b2*(q**2)) + a3*np.exp(-b3*(q**2)) + a4*np.exp(-b4*(q**2)) + a5*np.exp(-b5*(q**2))+c
    
    maffO = (1.0 + alphaO*np.exp(-(q**2)/(2*(delta**2))))*affO
    
    return maffO

def maffH(alphaH, delta, q):
    # Cromer-Mann coefficients from ruppweb
    a1 = 0.493
    a2 = 0.323
    a3 = 0.140
    a4 = 0.041
    b1 = 10.511
    b2 = 26.126
    b3 = 3.142
    b4 = 57.800
    c  = 0.003
    
    affH = a1*np.exp(-b1*(q**2)) + a2*np.exp(-b2*(q**2)) + a3*np.exp(-b3*(q**2)) + a4*np.exp(-b4*(q**2)) + c
    
    maffH = (1.0 + alphaH*np.exp(-(q**2)/(2*(delta**2))))*affH
    
    return maffH

