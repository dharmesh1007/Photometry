
"""           CALCULATE THE STAR MAGNITUDE AND ASSOCIATED ERROR                """
"""____________________________________________________________________________"""

"""
    To calculate the magnitude and associated error of your star the function 
    mag_calc requires the following parameters:
        
    + obj_count:    Counts of the star for which you require the magntitude.
                    Floating point decimal or integer will do.
    + obj_error:    Error in the number of counts of the star for which you 
                    require the magnitude.
    + std_count:    Counts of the standard star or stars used for magnitude
                    calculation. These should be provided in the form of a
                    floating point or integer, or a numpy 1D array of counts
                    for multiple standard stars.
    + std_error:    Error in the counts provided for std_count. Provide in the
                    same form as that provided for std_count.
    + std_mag:      Magnitudes of the standard star or stars used for the
                    calculation of the magnitude of your chosen star. These
                    should be provided in the form of a floating point or 
                    integer, or a numpy 1D array of counts for multiple 
                    standard stars.
    + std_magerr:   Error in magnitude of std_mag star or stars. Provide in the
                    same form as that provided for std_count.
                    
    
    The function uses the standard formula for the magnitude and standard 
    error propagation for the calculations of magnitude and associated error.
    
    The function returns the magnitude and associated error of your chosen star
    in the form of a tuple when only one standard star is given. Where multiple
    standard stars are given, mag_calc returns a tuple containing a numpy 2D
    array: ([[mag1, mag2, ...], [magerror1, magerror2, ...]]), where values 
    represent the magnitude or associated error calculated with each standard 
    star.
    
"""


import numpy as np

def mag_calc(obj_count, obj_error, std_count, std_error, std_mag, std_magerr):
    
    try:
        # Calculate magnitude
        mag = -2.5*np.log10(obj_count/std_count)+std_mag
        
        # Calculate magnitude error
        magerr = np.sqrt( (2.5/np.log(10))**2 * ((obj_error/obj_count)**2 +\
                           (std_error/std_count)**2) + std_magerr**2)
    except:
        mag = 0
        magerr = 0
    
    return mag, magerr 