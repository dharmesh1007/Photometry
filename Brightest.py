
"""   LOCATE BRIGHTEST PIXEL WITHIN SQUARE GRID CENTRED ON GIVEN COORDINATES   """
"""____________________________________________________________________________"""


"""
    Function requires following parameters:
    
    + imgdta:       specifically a 2D numpy array of the number of counts in
                    each pixel with indexing such that the y coordinate 
                    represents the first index and the x coordinate the second 
                    value. For example: imgdta[5,10] represents the number of 
                    counts in the pixel with the y coordinate 5 and x 
                    coordinate 10.
    + obj_xcoord:   an array or 1D numpy array of the x coordinates of the 
                    objects, in pixels, you wish to process 
    + obj_xcoord:   an array or 1D numpy array of the y coordinates of the 
                    objects, in pixels, you wish to process
    + pix_map_rad:  number of pixels either side above and below given object 
                    coordinates you wish to assess for brighter pixel.
    
    The resulting output is a list of two-tuples with tuples representing the
    best approximation of the exact coordinates of each object [(x1,y1, (x2,y2), ...]
"""

def brightestpixel(imgdta, obj_xcoord, obj_ycoord, pix_map_rad):
                    
    pix_val_new = []  # empty list ready for revised coordinates for aperture centre.
            
    for obj in range(0, len(obj_xcoord)):
        a = int(obj_xcoord[obj])  # object's x-coordinate as integer
        b = int(obj_ycoord[obj])  # object's y-coordinate as integer
        
        try:
            pix_map = []  # empty list for pixel counts in pixel grid
            pix_map_x = []  # empty list for x coordinate of grid
            pix_map_y = []  # empty list for y coordinate of grid
            for yshift in range(-pix_map_rad, pix_map_rad+1):  # grid y-range
                for xshift in range(-pix_map_rad, pix_map_rad+1):  # grid x-range
                    pix_map.append(imgdta[b + yshift, a + xshift])
                    pix_map_x.append(a + xshift)
                    pix_map_y.append(b + yshift)
            
            ind = pix_map.index(max(pix_map))  # index of brightest pixel
            
            """
            # TESTS TO CHECK FUNCTION OPERATION
            print(len(pix_map))     # How many pixels are examined
            print(max(pix_map))     # The maximum count in those pixels
            print(ind)              # index of max value in the list 'ind'
            print(pix_map_x[ind])   # x coordinate of max count in pixels
            print(pix_map_y[ind])   # y coordinate of max count in pixels
            # Check whether above is correct.
            print(imgdta[pix_map_y[ind], pix_map_x[ind]])
            """
            
            # Create a new coordinate tuple (x,y) in the pix_val_new list for
            # the revised coordinates.
            pix_val_new.append((pix_map_x[ind], pix_map_y[ind]))

        except:
            # otherwise create a coordinate tuple (x,y) within the list with
            # the original coordinates.
            pix_val_new.append((obj_xcoord[obj],obj_ycoord[obj]))

    return pix_val_new

