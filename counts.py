
"""           CALCULATE THE STAR COUNTS IN THE OBJECT APERTURE                 """
"""____________________________________________________________________________"""


"""
    The counts function requires the following parameters: 

    + imgdta:       specifically a 2D numpy array of the number of counts in
                    each pixel with indexing such that the y coordinate 
                    represents the first index and the x coordinate the second 
                    value. For example: imgdta[5,10] represents the number of 
                    counts in the pixel with the y coordinate 5 and x 
                    coordinate 10.
    + annulus:      an instance of one of the aperture classes from 
                    photutils.aperture.<chosen class> which requires the pixel 
                    coordinates of the aperture centre and the radius (in 
                    pixels) of the aperture.
    + annulus:      an instance of one of the aperture classes from 
                    photutils.aperture.<chosen class> which requires the pixel 
                    coordinates of the annulus centre and the inner and outer
                    radius (in pixels) of the annulus.
    + gain:         The number of electrons per ADU (analog to digital units).
    
    The star counts in the object aperture is found in the following way. Using
    the bkg_med function the sky counts per pixel is calculated, this is then 
    multiplied by the aperture area to find the sky counts in the object
    aperture.
    
    The aperture_photometry function then calculates the total counts in the
    object aperture from which the sky counts calculated above is subtracted.
    This leaves us with the star counts in the object aperture. Poisson
    statistics are then used to find the associated error in this value.
    
    The function returns the sky counts in the object aperture and the
    associated error in the form of a tuple.
"""

from background import bkg_med
from photutils import aperture_photometry
import numpy as np

def counts(imgdta, aperture, annulus, gain):
    
    # CALCULATION OF STAR COUNTS
    sky_ave = bkg_med(annulus, imgdta) # sky counts per pixel
    sky_aper = sky_ave*aperture.area # sky counts in aperture
    
    aper_phot = aperture_photometry(imgdta, aperture) # aperture photometry
    residual_count = aper_phot['aperture_sum']-sky_aper # sky subtracted counts
    
    # CALCULATION OF ERROR IN STAR COUNTS
    aper_sum = np.array(aper_phot['aperture_sum']) # total counts in aperture
    c_a = aper_sum # redefinition for formula
    c_b = sky_aper # redefinition of sky counts in aperture for formula
    scaled_area = aperture.area / annulus.area
    inv_sqrt_gain = gain ** (-1/2)
    error = ((c_a + c_b*scaled_area**2)**(1/2))*inv_sqrt_gain
    
    return np.array(residual_count), error
