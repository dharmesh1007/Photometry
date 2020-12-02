# Photometry
Contains tools for automating aperture photometry on multiple images (helpful for variable star astronomy)

To use just do the following:
  - download the repository to your local directory
  - Open whatever application you use to run python 3 code (e.g. Jupyter or Spyder)
  - Open the file test.py and run it
  - This will use functions contained in files within the same folder to calculate the magnitude of the target star in each of the images in the FITS folder
  - This will result in a plot of the light curve and the creation of a spreadsheet file which contains the raw magnitude data, together with associated errors.
  
  The files in the folder FITS are fits files from the Liverpool telescope SkyCam archive available at https://telescope.livjm.ac.uk/SkyCam/skycam_search.html.
  These images relate to the target star AG Pegasi, whose coordinates are contained within the variable obj_coords, along with coordinates of 5 standard stars.
  The right ascensions are given in the first array within the tuple, the declinations are given in the second list in that tuple. AG Pegasi (target star) coordinates
  are the first entries in each list. The standard star coordinates make up the remaining entries.
  
  The magnitudes produced are that of AG Pegasi, calculated using the standard stars given. The images are only a small sample of images of AG Pegasi taken during its
  2015 outburst.  To produce light curves of AG Pegasi or any star for that matter, one needs only to download the relevant FITS file date from the above link or from any
  other source and place it into the FITS folder then run the test.py code with necessary alterations. With respect to the Liverpool telescope AG Pegasi data, everything is
  set up such that you download FITS files into the FITS folder for the specific dates you want magnitude data from and run the code.
  
  Please note that one of the stars used for magnitude calculation is so bright and close to the target star that it effects the outcome of the magnitude calculation, therefore
  this standard star has been ommitted from the final calculations of magnitude (see code).
  
  The magnitudes are calculated with respect to the Sloan r' photometric band. Standard star data is available from the APASS all sky survey (https://www.aavso.org/apass).
  
  The code uses functions available in the subpackage called photutils contained in the core astropy package, along with some bespoke code specific to the calculation of
  AG Pegasi's magntiude.
