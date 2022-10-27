import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def do_histogram(a,bi,bf,db):
    '''
    finally a good histogram function
    '''
    bins = np.arange(bi-db/2.,bf+db/2.+db,db)
    y,x_tmp = np.histogram(a,bins=bins)
    x = np.array([(bins[j]+bins[j+1])/2. for j in range(len(bins)-1)])
    return x,y

def line(x,a,b):
    return a*x+b

def gaussian(x,a,b,c,d):
    # in this form the c is the FWHM
    return np.abs(a)*np.exp(-4*np.log(2)*(x-b)**2./(c**2))+d

def exponential(x,a,b,c):
    return np.abs(a)*np.exp(-x/(np.abs(b)))+c

def fit(function,x,y,p0=None,sigma=None,bounds=None):
    '''
    fits a function and return the fit resulting parameters and curve
    '''
    popt,pcov = curve_fit(function,x,y,p0=p0,sigma=sigma)
    #x = np.arange(0,1e4)
    curve = function(x,*popt)
    perr = np.sqrt(np.diag(pcov))
    return popt,x,curve,perr

def wavelength_(photon_energy):
    ELEMENTARY_CHARGE = 1.602176634E-19 # C
    SPEED_OF_LIGHT = 299792458 # m/s
    PLANCK_CONSTANT = 6.62607015E-34 # Js
    wavelength = PLANCK_CONSTANT*SPEED_OF_LIGHT/(photon_energy*ELEMENTARY_CHARGE)
    return wavelength