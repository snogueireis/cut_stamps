#########################################################
#           Cut a stamp from a FITS image               #
# 	Sandra Nogueira dos Reis, May 2016 @ Lisbon			#
#########################################################

import montage_wrapper as montage
import numpy as np

#constants
pix_size  = 199    #width of output image [pixels]
pix_scale = 0.06   #pixel scale [arcsec/pixel]
size = (pix_scale * pix_size)/3600   #width of output image [degrees]

#open and read the files
tbl              = "catalog.cat"
gal,field,ra,dec = np.loadtxt (tbl, dtype=str, usecols=(0,1,2,3), unpack=True)


galf   = gal.astype(float)
galaxy = galf.astype(int)
table  = open("cutted_gal.txt","w")
table.write("#galaxy \t field \t ra \t dec \n")
for ii in range(len(gal)):
	ra_center  = ra[ii].astype(float)
	dec_center = dec[ii].astype(float)
	if field[ii] == "GOODS-S":
		input_img = "hlsp_candels_hst_wfc3_gs-tot_f160w_v1.0_drz.fits"
		montage.mSubimage(input_img, str(galaxy[ii])+"_cut.fits", ra_center, dec_center, size)
		table.write(str(galaxy[ii])+"\t"+str(field[ii])+"\t"+str(ra_center)+"\t"+str(dec_center)+"\n")
	elif field[ii] == "GOODS-N":
		#input_img = "hlsp_candels_hst_wfc3_gn13_f160w_v0.5_drz.fits"
		input_img = "goodsn_all_wfc3_ir_f160w_060mas_v1.0_drz.fits"
		montage.mSubimage(input_img, str(galaxy[ii])+"_cut.fits", ra_center, dec_center, size)
		table.write(str(galaxy[ii])+"\t"+str(field[ii])+"\t"+str(ra_center)+"\t"+str(dec_center)+"\n")
	elif field[ii] == "COSMOS":
		input_img = "hlsp_candels_hst_wfc3_cos-tot_f160w_v1.0_drz.fits"
		montage.mSubimage(input_img, str(galaxy[ii])+"_cut.fits", ra_center, dec_center, size)
		table.write(str(galaxy[ii])+"\t"+str(field[ii])+"\t"+str(ra_center)+"\t"+str(dec_center)+"\n")
	elif field[ii] == "UDS":
		input_img = "hlsp_candels_hst_wfc3_uds-tot_f160w_v1.0_drz.fits"
		montage.mSubimage(input_img, str(galaxy[ii])+"_cut.fits", ra_center, dec_center, size)
		table.write(str(galaxy[ii])+"\t"+str(field[ii])+"\t"+str(ra_center)+"\t"+str(dec_center)+"\n")
	elif field[ii] == "AEGIS":
		#input_img = "hlsp_candels_hst_wfc3_egsb02_f160w_v0.5_drz.fits"
		input_img = "egs_all_wfc3_ir_f160w_060mas_v1.0_drz.fits"
		montage.mSubimage(input_img, str(galaxy[ii])+"_cut.fits", ra_center, dec_center, size)
		table.write(str(galaxy[ii])+"\t"+str(field[ii])+"\t"+str(ra_center)+"\t"+str(dec_center)+"\n")
table.close()
