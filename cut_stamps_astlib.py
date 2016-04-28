########################################################
# Cut a galaxy from a FITS file with an updated header #
# Author: S. N. dos Reis        					   #
# Date: April 2016									   #
########################################################

import pyfits
import pywcs
import numpy as np
from astLib import astImages
from astLib import astWCS


#constants
my_galaxy = '1'

#Read the output table from SExtractor
tbl   = "gs.cat"
table = np.loadtxt(tbl)

#Open and read
hdulist = pyfits.open("gs_all_candels_ers_udf_f160w_060mas_v0.5_drz.fits")
hdr = hdulist[0].header
img = hdulist[0].data

#Create wcs object
wcs = astWCS.WCS(hdr, mode = "pyfits")

#Read the position of the galaxy
xx = table[0,1]
yy = table[0,2]

#Transform from pixels to decimal
coords = astWCS.WCS.pix2wcs(wcs,xx,yy)
ra     = coords[0]
dec    = coords[1]

#cut the stamp
my_new_image = astImages.clipImageSectionWCS(img, wcs, ra, dec, 0.001667, returnWCS=True)

#write FITS file
data     = my_new_image['data']
imagewcs = my_new_image['wcs']
astImages.saveFITS(my_galaxy+".fits", data, imagewcs)
