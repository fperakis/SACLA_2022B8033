import numpy as np
from exp_parameters import *

#* Implementation notes: run
# * --------------------------------------------------------------
# * Calculates iteratively the Knudsen evaporation rate with
# * surface tension modification to the saturated vapor pressure
# * from the Kelvin equation, calculates the heat conduction
# * through the droplet via Fourier's law (given the input number
# * of shells), calculates the mass-loss due to evaporation.
# * Outputs the mass-averaged temperature of the droplet as a
# * function of travel time.

def EvapCool_run(save_dir, r0, NShell, dt, NSteps, Nout, g, T0, P0, DHalgorithm, Cpalgorithm, rhoalgorithm, Pvapalgorithm, kappaalgorithm, taualgorithm):    
    
# ---------------- run parameters ------------------------
    
#  write out all relevant settings
   # print("#   Evaporative cooling of water droplets: %s initial settings" %configFile)
    print("#   --------------------------------------------------------------------")
    print("#   Droplet radius         r0 = %.3f um" %(r0*1e6))
    print("#   Initial temperature    T0 = %.3f K" %T0)
    print("#   Backpressure           P0 = %.3f Pa" %P0)
    print("#   Time step              dt = %.3f ns" %(dt*1e9))
    print("#   Number of shells   NShell = %d" %NShell)
    print("#   Number of steps    NSteps = %d" %NSteps)
    print("#   Evaporation coeff   gamma = %.1f" %g)
    #print("#   Shell output        scale = %.1f" %scale) # not used

    if (DHalgorithm == 1):
        print("#   Hvap  -- taken from Somayujulu, Int. J. Thermophysics 9, 567 (1988)")
    elif (DHalgorithm == 2):
        print("#   Hvap  -- taken from Murphy & Koop, Quarterly Journal of the Royal Meteorological Society 131, 1539 (2005)")
    elif (DHalgorithm == 3):
        print("#   Hvap  -- polynomial (T^5) fit to TIP4P/2005 simulation")
    elif (DHalgorithm == 4):
        print("#   Hvap  -- polynomial (T^5) fit to TIP4P/2005 simulation scaled by 0.9701 to fit experiment at r.t.")
    else:
        print("#   Hvap  -- taken from Somayujulu, Int. J. Thermophysics 9, 567 (1988)")
              
    if (Cpalgorithm == 1):
        print("#   Cp    -- taken from Angell, JPC 86, 998 (1982)")
    elif (Cpalgorithm == 2):
        print("#   Cp    -- taken from Huang & Bartell, JPC 99, 3924 (1995)")
    elif (Cpalgorithm == 3):
        print("#   Cp    -- taken from Oguni, JCP 73, 1948 (1980)")
    elif (Cpalgorithm == 4):
        print("#   Cp    -- constant (75.5 J/mol/K)")
    elif (Cpalgorithm == 5):
        print("#   Cp    -- polynomial (T^6) fit to experiment taken from Angell, JPC 86, 998 (1982)")
    elif (Cpalgorithm == 6):
        print("#   Cp    -- power law fit (Ts = 226 K) to experiment taken from Angell, JPC 86, 998 (1982)")
    elif (Cpalgorithm == 7):
        print("#   Cp    -- polynomial (T^8) fit to TIP4P/2005 simulation")
    elif (Cpalgorithm == 8):
        print("#   Cp    -- polynomial (T^8) fit to TIP4P/2005 simulation scaled by 0.8258 to fit experiment at r.t.")
    else:
        print("#   Cp    -- taken from Angell, JPC 86, 999 (1982)")

    if (rhoalgorithm == 1):
        print("#   rho   -- interpolation of experimental density data of ice (Ih = 0.934 g/cm^3) and water taken from Kell, Journal of Chemical Engineering Data 20, 97 (1975)")
    elif (rhoalgorithm == 2):
        print("#   rho   -- taken from Hare & Sorensen, JCP 87, 4840 (1987)")
    elif (rhoalgorithm == 3):
        print("#   rho   -- polynomial (T^6) fit to TIP4P/2005 simulation")
    elif (rhoalgorithm == 4):
        print("#   rho   -- polynomial (T^6) fit to TIP4P/2005 simulation scaled by 1.002 to reproduce experimental density maximum")
    else:
        print("#   rho   -- interpolation of experimental density data of ice (Ih = 0.934 g/cm^3) and water taken from Kell, Journal of Chemical Engineering Data 20, 97 (1975)")

    if (Pvapalgorithm == 1):
        print("#   Psat  -- taken from Murphy & Koop, Quarterly Journal of the Royal Meteorological Society 131, 1539 (2005)")
    elif (Pvapalgorithm == 2):
        print("#   Psat  -- taken from Hyland & Wexler, Special publication of the American Society of Heating, Project 216 (1982)")
    elif (Pvapalgorithm == 3):
        print("#   Psat  -- taken from Buck, Buck Research CR-1A User's Manual, Appendix 1 (1996)")
    elif (Pvapalgorithm == 4):
        print("#   Psat  -- recommended by WMO (2000), originally published by Goff, Transactions of the American Society of Heating and Ventilating Engineers, 347 (1957)")
    else:
        print("#   Psat  -- taken from from Murphy & Koop, Quarterly Journal of the Royal Meteorological Society 131, 1539 (2005)")

    if (kappaalgorithm == 1):
        print("#   kappa -- polynomial (T^4) fit to experiment taken from CRC Handbook of Chemistry and Physics, 2nd ed., E-10")
    elif (kappaalgorithm == 2):
        print("#   kappa -- taken from Ramires, NIST (1994)")
    else:
        print("#   kappa -- polynomial (T^4) fit to experiment taken from CRC Handbook of Chemistry and Physics, 2nd ed., E-10")

    if (taualgorithm == 1):
        print("#   tau   -- taken from Floriano & Angell, JCP 94, 10 (1990)")
    else:
        print("#   tau   -- taken from Floriano & Angell, JCP 94, 10 (1990)")

    print("#   --------------------------------------------------------------------")
    print("#   t [s]; T(t) [K]")

    # change precision of output
    # typedef numeric_limits<double> dbl;
    # cout.precision(dbl::digits10);
    
    
# ---------------- Physical constants --------------------

    # physical constants in SI units, NIST website
    NA      = 6.02214129e23                      # Avogadro's constant in 1/mol
    kB      = 1.3806488e-23                       # Boltzmann constant J/K
    Rgas    = 8.3144621                           # universal gas constant J/mol/K	
    molmass = 0.01801528                          # molecular mass of water in kg/mol
    mmolec  = molmass / NA                        # mass of one water molecule in kg
    fpi     = 4.0 * np.pi                         # frequently used constant (4*pi)
    RATE_CONST = 1 / np.sqrt(fpi * mmolec * kB / 2.0) # constant term in evaporation rate

    
# ---------------- Variable initialization ------------------

    outfreq  = int(np.round(NSteps/Nout)) # round up: (int) ceil(NSteps / (double) Nout)
    Tsurf    = T0
    dTsurf   = 0.0
    IntGamma = 0.0
    dr       = r0 / NShell
    Area     = np.pi * r0 * r0
    dVsurf   = fpi * (r0 * r0 * r0 - (r0 - dr) * (r0 - dr) * (r0 - dr)) / 3.0 
    
    # output arrays
    timearr = np.empty(NSteps // outfreq - 1)
    Tavearr = np.empty(NSteps // outfreq - 1)
    massarr = np.empty(NSteps // outfreq - 1)
    radarr = np.empty(NSteps // outfreq - 1)
    #Tgradarr = np.empty((NSteps // outfreq - 1)*NShell+1) # commented out by sharon
    # Tgradarr = np.empty[outfreq]
    
    # heat conduction variables	
    rad = np.empty(NShell+1) # outer shell radius
    for i in range(NShell+1):
        rad[i] = i*dr
    
    radm = np.empty(NShell+1) # inner shell radius
    for i in range(1, NShell+1):
        radm[i] = (i - 1) * dr
    radm[0] = 0.0
    
    rnew    = r0
    
    dV = np.empty(NShell+1) # shell volumina
    for i in range(NShell+1):
        dV[i] = fpi * (rad[i] * rad[i] * rad[i] - radm[i] * radm[i] * radm[i]) / 3.0 

    # array for the updated time step
    Tn = np.zeros(NShell+1)
    
    # initial condition: homogeneous temperature distribution
    Tm = np.ones(NShell+1)*T0

    # array for mass of individual shells for mass averaging of temperature
    mshell = np.zeros(NShell+1)

    # Calculations for evaporative cooling, including evaporation, 
    # heat conduction, mass loss, surface tension modification of vapor pressure

    for i in range(1,NSteps):

    # EVAPORATION ---------------------------------------------
        
        #calculate Knudsen evaporation rate [1/s]

        # without surface tension modification of Pvap
        #Gamma       =  Pvap(Tsurf, P0, Pvapalgorithm) * g * RATE_CONST * Area / sqrt(Tsurf) 

        # with surface tension modification of Pvap
        Gamma       =  Pvap(Tsurf, P0, Pvapalgorithm) * g * RATE_CONST * Area * np.exp(2.0 * surf_tension(Tsurf, taualgorithm) * molmass / (density(Tsurf, rhoalgorithm) * rnew * Rgas * Tsurf)) / np.sqrt(Tsurf)
        
        # temperature change of the evaporation shell [K]
        dTsurf      = - Gamma * (enthalpy_vap(Tsurf, DHalgorithm) / NA) * dt / ((heat_capacity(Tsurf, Cpalgorithm) / molmass) * dVsurf * density(Tsurf, rhoalgorithm))
        
        # integrate rate to obtain amount of particles lost [unitless]
        IntGamma   +=  Gamma * dt                                                      

        # update surface temperature after evaporation
        Tm[NShell]  = Tsurf + dTsurf

         #------------------------ heat conduction, loop over shells --------------------------------------

        for j in range(1, NShell):

            # calculate temperature gradients between shells
            dTl   = - Tm[j] + Tm[j - 1] # temp gradient, left shell boundary
            dTr   =   Tm[j] - Tm[j + 1] # temp gradient, right shell boundary

            # difference between heat gain and heat loss for each shell (Fourier's law)
            dQ    = fpi * dt * (thermal_cond(Tm[j], kappaalgorithm) * rad[j] * radm[j] * dTl - thermal_cond(Tm[j + 1], kappaalgorithm) * rad[j + 1] * radm[j + 1] * dTr) / dr

            # temperature change in each shell due to change of heat, array update
            dTemp = dQ / ((heat_capacity(Tm[j], Cpalgorithm) / molmass) * dV[j] * density(Tm[j], rhoalgorithm)) 
            Tn[j] = Tm[j] + dTemp


        # innermost shell: only heat loss, no gain 
        dTr        = Tm[0] - Tm[1]
        dQ         = - fpi * thermal_cond(Tm[0], kappaalgorithm) * rad[1] * rad[1] * dTr * dt / dr
        dTemp      = dQ / ((heat_capacity(Tm[0], Cpalgorithm) / molmass) * dV[1] * density(Tm[0], rhoalgorithm))
        Tn[0]      = Tm[0] + dTemp
        
        # outermost shell: only heat gain from conduction, no loss (only via evaporation)
        dTl        = - Tm[NShell] + Tm[NShell - 1]
        dQ         = fpi * thermal_cond(Tm[NShell], kappaalgorithm) * rad[NShell - 1] * radm[NShell - 1] * dTl * dt / dr
        dTemp      = dQ / ((heat_capacity(Tm[NShell], Cpalgorithm) / molmass) * dV[NShell] * density(Tm[NShell], rhoalgorithm))
        Tn[NShell] = Tm[NShell] + dTemp


        # temperature output for all shells individually before mass-weighted averaging
        #if (i % outfreq == 0): #{             # modulus division - commented our by sharon - not used
        
           # for (int l = 0; l < NShell; ++l) {
         #   for l in range(NShell): # commented out by sharon
                
               # Tgradarr[(i // outfreq - 1) * NShell + l] = Tn[l] # commented out by sharon
    
           # } # for l

        #} # if


        # mass-weighted averaging over the shells' temperatures
        Tave = 0.0
        mtot = 0.0
        
        for k in range(NShell):
            
            mshell[k] = dV[k] * density(Tn[k], rhoalgorithm)
            Tave     += Tn[k] * mshell[k]
            mtot     += mshell[k]
            

        Tave = Tave / mtot


        # output
        if (i % outfreq == 0):       # modulus division

            print(i * dt, "   ", Tave) # print temperature vs time

            timearr[i // outfreq - 1] = i * dt
            Tavearr[i // outfreq - 1] = Tave
            radarr[i // outfreq - 1]  = rnew
            massarr[i // outfreq - 1] = currelnum

        
# ---------------------------- Mass loss due to evaporation ----------------------------------------- 
        

        # update geometrical properties due to massloss

        # current relative number of molecules in the droplet and initial number
        currelnum = 1.0 - 3.0 * mmolec * IntGamma / (fpi * r0 * r0 * r0 * density(Tave, rhoalgorithm))
        
        # rnew = r0 # test without massloss
        rnew = (r0 * r0 * r0 * currelnum)**(1.0 / 3.0)
        # rnew   = (r0 * r0 * r0 - 3.0 * mmolec * IntGamma / (fpi * density(Tave, rhoalgorithm)))**(1.0 / 3.0)
        dr     = rnew / NShell

        for i in range(NShell+1):
            rad[i] = i * dr

        for i in range(NShell+1):
            radm[i] = (i - 1) * dr

        radm[0] = 0.0
        Area    = fpi * rnew * rnew

        for i in range(NShell+1):
            dV[i] = fpi * (rad[i] * rad[i] * rad[i] - radm[i] * radm[i] * radm[i]) / 3.0
        
        dVsurf = fpi * (rnew * rnew * rnew - (rnew - dr) * (rnew - dr) * (rnew - dr)) / 3.0

        # update surface and shell temperatures 
        Tsurf = Tn[NShell]
        # Tsurf = Tm[NShell]  # test for evaporation ALONE!

        for j in range(NShell+1):
            Tm[j] = Tn[j]

    
    print("#   --------------------------------------------------------------------")
    
    # added by sharon:
    # save data:
    np.save(save_dir+'/time', timearr)
    np.save(save_dir+'/Tave', Tavearr)
    np.save(save_dir+'/rad', radarr)
    np.save(save_dir+'/mass', massarr)

    #return 0
    return timearr, Tavearr
