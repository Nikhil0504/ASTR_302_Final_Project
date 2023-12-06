#!/bin/sh
export filter=f090w
export gain=2576.82
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../PSFs/images/${filter}_degrade_f444w_reproject.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht_reproject.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

export filter=f150w
export gain=2061.46
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../PSFs/images/${filter}_degrade_f444w_reproject.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht_reproject.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

export filter=f200w
export gain=3435.768
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../PSFs/images/${filter}_degrade_f444w_reproject.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht_reproject.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

export filter=f277w
export gain=3435.768
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../PSFs/images/${filter}_degrade_f444w.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

export filter=f356w
export gain=2061.46
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../PSFs/images/${filter}_degrade_f444w.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

export filter=f444w
export gain=2576.83
sex ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits -c g165_sed_basic.sex -CATALOG_NAME ../../sextractor/F444W/$filter.cat -GAIN $gain -WEIGHT_IMAGE ../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits,../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-${filter}/jw04446-c1000_t009_nircam_clear-${filter}_i2d_wht.fits -WEIGHT_TYPE MAP_WEIGHT,MAP_WEIGHT -WEIGHT_GAIN Y,Y

