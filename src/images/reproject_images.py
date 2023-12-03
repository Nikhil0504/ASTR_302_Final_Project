from astropy.io import fits
from reproject import reproject_interp

def reproject_images(hdu1, hdu2):
    array, _ = reproject_interp(hdu2, hdu1.header)
    hdu = fits.PrimaryHDU()
    hdu.data = array
    hdu.header = hdu1.header
    return hdu


if __name__ == '__main__':
    hdu1 = fits.open('../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-f444w/jw04446-c1000_t009_nircam_clear-f444w_i2d_sci.fits')[0]

    filters = ['f090w', 'f150w', 'f200w']
    for filt in filters:
        # hdu2 = fits.open('../../PSFs/images/{}_degrade_f444w.fits'.format(filt))[0]
        hdu2 = fits.open(f'../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-{filt}/jw04446-c1000_t009_nircam_clear-{filt}_i2d_wht.fits')[0]
        hdu = reproject_images(hdu1, hdu2)
        # hdu.writeto('../../PSFs/images/{}_degrade_f444w_reproject.fits'.format(filt), overwrite=True)
        hdu.writeto(f'../../../Data/MAST_2023-12-03T1249/JWST/jw04446-c1000_t009_nircam_clear-{filt}/jw04446-c1000_t009_nircam_clear-{filt}_i2d_wht_reproject.fits', overwrite=True)