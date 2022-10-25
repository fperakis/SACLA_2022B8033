import numpy as np

# Functions for experimental parameters

# Implementation notes: DH
# Calculates the enthalpy of vaporization [J/mol] of water for a given temperature T [K].
    
def enthalpy_vap(T, algorithm=1):
    
# enthalpy of vap of water in J/mol: DH

# temperature of triple point for water in K
    Tt = 273.16;
    
# critical temperature of the gas-liquid critical point for water in K
    Tc = 647.126;

# reduced temperature w.r.t. the critical temperature
    X = (Tc - T)/(Tc - Tt)

    if (algorithm == 1):
# ALGORITHM 1 -- taken from Somayujulu, Int. J. Thermophysics 9, 567 (1988)
        DH = 1000*(44.457979*X**(3.0/8.0) + 14.635863*X**(1.0 + 3.0/8.0) - 27.945633*X**(2.0 + 3.0/8.0) + 13.985176*X**(3.0 + 3.0/8.0))                                             
    elif (algorithm == 2): 
# ALGORITHM 2 -- taken from Murphy & Koop, Quarterly Journal of the Royal Meteorological Society 131, 1539 (2005)
        DH = 56579.0 - 42.212*T + np.exp(0.1149*(281.6 - T))
    elif (algorithm == 3): 
# ALGORITHM 3 -- polynomial (T^5) fit to TIP4P/2005 simulation
        DH = 1000*(-187.44 + 4.70*T - 0.034769*T**2 + 0.00012385*T**3 - 2.1674E-7*T**4 + 1.4959e-10*T**5)
    elif (algorithm == 4): 
# ALGORITHM 4 -- polynomial (T^5) fit to TIP4P/2005 simulation scaled by 0.9701 to fit experiment at r.t.
        DH = 0.9701*1000*(-187.44 + 4.70*T - 0.034769*T**2 + 0.00012385*T**3 - 2.1674e-7*T**4 + 1.4959e-10*T**5)

    return(DH)

#############################################################
# Implementation notes: Cp
# Calculates the specific heat capacity [J/mol/K] of water for a given temperature T [K].

def heat_capacity(T, algorithm=1):
	
# heat capacity of water in J/mol/K: Cp

    if (algorithm == 1): 
    # ALGORITHM 1 -- taken from Angell, JPC 86, 998 (1982)
        Cp = 75.379992 + 80.5428*np.exp(0.110358*(226 - T))
    elif (algorithm == 2):
    # ALGORITHM 2 -- taken from Huang & Bartell, JPC 99, 3924 (1995)
        Cp = 72.92 + 0.01896 * (T - 226.0) + 41.7 / (1.0 + 0.0072 * (T - 226.0) * (T - 226.0))
    elif (algorithm == 3):
    # ALGORITHM 3 -- taken from Oguni, JCP 73, 1948 (1980)
        Cp = 67.85 + 2.309*(T/226.4 - 1.0)**(-0.933)
    elif (algorithm == 4):
    # ALGORITHM 4 -- constant (75.5 J/mol/K)
        Cp = 75.5
    elif (algorithm == 5):
    # ALGORITHM 5 -- polynomial (T^6) fit to experiment taken from Angell, JPC 86, 998 (1982)
        Cp = 0.5*(-4.918446910069158e-7*T**5 + 6.629043740464008e-004*T**4 - 0.357231756477509*T**3 + 96.219313730883627*T**2 - 1.295443543210677e+004*T + 6.975758920548891e+005 
                  + 1.796958801996025e-008*T**6 - 2.880415435149749e-005*T**5 + 0.019229566288177*T**4 - 6.843917968834040*T**3 + 1.369622281156036e+003*T**2 - 1.461343975335083e+005*T + 6.494963597586376e+006)
    elif (algorithm == 6):
    # ALGORITHM 6 -- power law fit (Ts = 226 K) to experiment taken from Angell, JPC 86, 998 (1982)
        Cp = 72.15583622 + 0.4398394*(T/226.0 - 1.0)**(-1.36432632)
    elif (algorithm == 7):
    # ALGORITHM 7 -- polynomial (T^8) fit to TIP4P/2005 simulation
        Cp = -0.2928*((T - 285.0)/53.3854)**8.0 + 1.7135*((T - 285.0)/53.3854)**7.0 - 2.4772*((T - 285.0)/53.3854)**6.0 - 1.2963*((T - 285.0)/53.3854)**5.0
        + 6.2057*((T - 285.0)/53.3854)**4.0 - 5.8421*((T - 285.0)/53.3854)**3.0 + 3.7122*((T - 285.0)/53.3854)**2.0 - 7.3977*(T - 285.0)/53.3854 + 91.0656
    elif (algorithm == 8):
    # ALGORITHM 8 -- polynomial (T^8) fit to TIP4P/2005 simulation scaled by 0.8258 to fit experiment at r.t.
        Cp = 0.8258*(-0.2928*((T - 285.0)/53.3854)**8.0 + 1.7135*((T - 285.0)/53.3854)**7.0 - 2.4772*((T - 285.0)/53.3854)**6.0 - 1.2963*((T - 285.0)/53.3854)**5.0
                     + 6.2057*((T - 285.0)/53.3854)**4.0 - 5.8421*((T - 285.0)/53.3854)**3.0 + 3.7122*((T - 285.0)/53.3854)**2.0 - 7.3977*(T - 285.0)/53.3854 + 91.0656)                                   

    return(Cp)


################################################

# Implementation notes: rho
# Calculates the density [kg/m^3] of water for a given temperature T [K].

def density(T, algorithm=1):

# density of water in kg/m^3: rho

    if (algorithm == 1):
    # ALGORITHM 1 -- interpolation of experimental density data of ice (Ih = 0.934 g/cm^3) and water taken from Kell, Journal of Chemical Engineering Data 20, 97 (1975)
        rho = 933.942 + 66.7829 / (1.0 + np.exp( - 0.10662 * (T - 233.0573)))
    elif (algorithm == 2):
    # ALGORITHM 2 -- taken from Hare & Sorensen, JCP 87, 4840 (1987)
        rho = 1000*(0.99986 + 6.69e-5*(T - 273.15) - 8.486e-6*(T - 273.15)*(T - 273.15) + 1.518e-7*(T - 273.15)*(T - 273.15)*(T - 273.15) - 6.9484e-9*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15) 
                - 3.6449e-10*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15) - 7.497e-12*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15)*(T - 273.15))
    elif (algorithm == 3):
    # ALGORITHM 3 -- polynomial (T^6) fit to TIP4P/2005 simulation
        rho = 199154.0 - 4798.08*T + 49.2902*T**2 - 0.278943*T**3 + 0.000940308*T**4 - 1.88965e-6*T**5 + 2.09734e-9*T**6 - 9.92214E-13*T**7
    elif (algorithm == 4):
    # ALGORITHM 4 -- polynomial (T^6) fit to TIP4P/2005 simulation scaled by 1.002 to reproduce experimental density maximum
        rho = 1.002*(199154.0 - 4798.08*T + 49.2902*T**2 - 0.278943*T**3 + 0.000940308*T**4 - 1.88965e-6*T**5 + 2.09734e-9*T**6 - 9.92214e-13*T**7)

    return(rho)


###################################################


# Implementation notes: Pvap
# Calculates the effective vapor pressure [Pa] of water from the droplet for a given temperature T [K] and backpressure in the chamber P0.

def Pvap(T, P0, algorithm=1):
    
# effective vapor pressure in Pa for supercooled water from the droplet: Pvap

# saturation (i.e. equilibrium) vapor pressure in Pa for supercooled water: Psat

# backpressure in the vacuum chamber: P0

# temperature of triple point for water in K
    Tt = 273.16;

# see http://cires.colorado.edu/~voemel/vp.html for summary of empirical expressions
    if (algorithm == 1):
    # ALGORITHM 1 -- taken from from Murphy & Koop, Quarterly Journal of the Royal Meteorological Society 131, 1539 (2005)
        Psat = np.exp(54.842763 - 6763.22/T - 4.210*np.log(T) + 0.000367*T + np.tanh(0.0415*(T - 218.8))*(53.878 - 1331.22/T - 9.44523*np.log(T) + 0.014025*T))
    elif (algorithm == 2):
    #ALGORITHM 2 -- taken from Hyland & Wexler, Special publication of the American Society of Heating, Project 216 (1982)
        Psat = np.exp(-0.58002206e4/T + 1.3914993 - 0.48640239e-1*T + 0.41764768e-4*T**2 - 0.14452093e-7*T**3 + 6.5459673*np.log(T))
    elif (algorithm == 3):
    # ALGORITHM 3 -- taken from Buck, Buck Research CR-1A User's Manual, Appendix 1 (1996)
        Psat = 611.21 * np.exp((18.678 - (T - 273.15)/234.5)*(T - 273.15)/(T - 16.01))
    elif (algorithm == 4):
    # ALGORITHM 4 -- recommended by WMO (2000), originally published by Goff, Transactions of the American Society of Heating and Ventilating Engineers, pp. 347 (1957)
        Psat = 100*10**((10.79574*(1 - Tt/T) - 5.02800*np.log10(T/Tt)+ 1.50475e-4*(1 - 10**(-8.2969*(T/Tt - 1))) 
                        + 0.42873e-3*(10**(4.76955*(1 - Tt/T)) - 1) + 0.78614))

# calculate the effective vapor pressure by subtracting the backpressure in the vacuum chamber (assumes it is all H2O)
    Pvap = Psat - P0

    return(Pvap)


##########################################################

# Implementation notes: kappa
# Calculates the thermal conductivity [W/m/K] of water for a given temperature T [K].

def thermal_cond(T, algorithm=1):

# thermal conductivity of water in W/m/K

    if (algorithm == 1):
    # ALGORITHM 1 -- polynomial (T^4) fit to experiment taken from CRC Handbook of Chemistry and Physics, 2nd ed., E-10
    # experimental data in the temperature range 250 K ≤ T ≤ 640 K)
        kappa = 0.1*((8.311169571874185e-12)*T**4 + (2.795759096697513e-8)*T**3 - (1.052493788349872e-4)*T**2 + 0.069481082649479*T - 6.093514692522149)
    elif (algorithm == 2):
    # ALGORITHM 2 -- taken from Ramires, NIST (1994)
    # expression recommended for 274 K ≤ T ≤ 370 K
    # thermal conductivity of water at r.t. 0.6065 +/- 0.0036 W/m/K
        kappa = 0.6065*(-1.48445 + 4.12292*T/298.15 - 1.63866*(T/298.15)*(T/298.15))

    return(kappa)
    
    
############################################################
    
# Implementation notes: tau
# Calculates the surface tension [N/m] of water for a given temperature T [K]: tau

def surf_tension(T, algorithm=1):

    # surface tension in N/m: tau

    if (algorithm == 1):
    # ALGORITHM 1 -- taken from Floriano & Angell, JCP 94, 10 (1990)
    # linear fit to data
        tau = (75.643 - 0.15186*(T - 273.15))*0.001

    return(tau)