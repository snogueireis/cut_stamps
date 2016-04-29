########################################################
# Cut a galaxy from a FITS file with an updated header #
# Author: S. N. dos Reis                               #
# Date: April 2016									                #
########################################################

import pyfits
import pywcs
import numpy as np
from astLib import astImages
from astLib import astWCS


#constants
lim = 99

#Read the output table from SExtractor
tbl   = "gs.cat"
gal,xx,yy,mag_aper,flux_aper,fluxerr_aper,flux_auto,fluxerr_auto,ra,dec,fwhm,sm_sex,xmin,xmax,ymin,ymax = np.loadtxt(tbl, unpack = True)

#Open and read
hdulist = pyfits.open("gs_all_candels_ers_udf_f160w_060mas_v0.5_drz.fits")
hdr = hdulist[0].header
img = hdulist[0].data

#Create wcs object
wcs = astWCS.WCS(hdr, mode = "pyfits")

for ii in range(len(gal)):
    if ii <= lim:
      #Transform from pixels to decimal
      coords = astWCS.WCS.pix2wcs(wcs,xx[ii],yy[ii])
      ra     = coords[0]
      dec    = coords[1]

      #cut the stamp
      my_new_image = astImages.clipImageSectionWCS(img, wcs, ra, dec, 0.001667, returnWCS=True)

      #write FITS file
      data     = my_new_image['data']
      imagewcs = my_new_image['wcs']
      iii = ii + 1
      astImages.saveFITS('%s'%iii+".fits", data, imagewcs)
