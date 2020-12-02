
"""           CALCULATE THE AVERAGE COUNT PER BACKGROUND PIXEL                 """
"""____________________________________________________________________________"""


"""
    Sigma clipped median and the mean average background counts per pixel 
    require:
        
    + imgdta:       specifically a 2D numpy array of the number of counts in
                    each pixel with indexing such that the y coordinate 
                    represents the first index and the x coordinate the second 
                    value. For example: imgdta[5,10] represents the number of 
                    counts in the pixel with the y coordinate 5 and x 
                    coordinate 10.
    + annulus:      this would be an instance of one of the aperture classes
                    from photutils.aperture.<chosen class> which requires the
                    pixel coordinates of the annulus centre and the inner and
                    out radius (in pixels) of the annulus.
    
    The sigma clipped background calculation creates a template of the annulus
    over the image. Only pixels within this template are used in the 
    calculation of background counts, so fractions of pixels count 0 towards
    the sigma clipped median background count.
    
    Mean average background count just sums up counts of each pixel within the
    annulus and divides by the annulus area.
    
    Both functions return a numpy 1D array of the specified average background
    count per pixel for each of the object coordinates given.
"""

# IMPORTS
from astropy.stats import sigma_clipped_stats
from photutils import aperture_photometry
import numpy as np

# SIGMA CLIPPED MEDIAN BACKGROUND COUNT PER PIXEL
def bkg_med(annulus, imgdta):
    
    annulus_masks = annulus.to_mask(method='center')
    bkg_median = []
    
    for mask in annulus_masks:
        try:
            annulus_data = mask.multiply(imgdta)
            annulus_data_1d = annulus_data[mask.data > 0]
            _, median_sigclip, _ = sigma_clipped_stats(annulus_data_1d)
            bkg_median.append(median_sigclip)
        except:
            bkg_median.append(0)
    
    return np.array(bkg_median)


# MEAN AVERAGE BACKGROUND COUNT PER PIXEL
def bkg_mean(annulus, imgdta):
    
    phot_table = aperture_photometry(imgdta, annulus)
    mean = phot_table['aperture_sum'] / annulus.area
    
    mean_array=[]
    
    for i in range(0, len(mean)):
        mean_array.append(mean[i])
        
    return np.array(mean_array)



