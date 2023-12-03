# f090w - 0.03, f150w - 0.03, f200w - 0.03, f277w - 0.06, f356w - 0.06, f444w - 0.06
import pathlib

import numpy as np

from astropy.io import fits
from astropy.convolution import convolve_fft
from photutils.psf import CosineBellWindow, create_matching_kernel
from photutils.psf.matching import resize_psf

from scipy.ndimage import rotate


# Paths
MAIN_PATH = pathlib.Path('../../PSFs')
IMAGE_PATH = pathlib.Path("../../../Data/MAST_2023-12-03T1249/JWST")

hi_filter = 'f356w'
low_filter = 'f444w'

IMAGE = str(IMAGE_PATH / f'jw04446-c1000_t009_nircam_clear-{hi_filter}/jw04446-c1000_t009_nircam_clear-{hi_filter}_i2d_sci.fits')

# QUALITY PSF1 > PSF2 (we will need to degrade PSF1 to PSF2)
PSF1 = str(MAIN_PATH / f'webbpsf/webb_psf_{hi_filter.upper()}.fits')
PSF2 = str(MAIN_PATH / f'webbpsf/webb_psf_{low_filter.upper()}.fits')

print(f'{hi_filter} to {low_filter}')

psf2 = fits.open(PSF2)[0]
# psf2 = np.mean(psf2, axis=0)

# rotate to match image
psf2_rot = rotate(psf2.data, 138.378, reshape=False)
psf2_rot = resize_psf(psf2_rot, psf2.header['PIXELSCL'], 0.0598)


psf1 = fits.open(PSF1)[0]
psf1_rot = rotate(psf1.data, 138.378, reshape=False) # get from JWST Image header 'PA_APPER'
psf1_rot = resize_psf(psf1_rot, psf1.header['PIXELSCL'], 0.0601)

print(psf2_rot.shape, psf1_rot.shape)
# psf2_rot = np.pad(psf2_rot, (41, 41))

image = fits.open(IMAGE)[0].data

psf2_rot /= psf2_rot.sum()
psf1_rot /= psf1_rot.sum()

window = CosineBellWindow(alpha=0.9)
kernel = create_matching_kernel(target_psf=psf2_rot, source_psf=psf1_rot, window=window)
conv_im = convolve_fft(np.nan_to_num(image), kernel, allow_huge=True)

hdu = fits.PrimaryHDU()
hdu.data = conv_im
hdu.header = fits.open(IMAGE)[0].header
hdu.writeto(f'{MAIN_PATH}/images/{hi_filter}_degrade_{low_filter}.fits', overwrite=True)

