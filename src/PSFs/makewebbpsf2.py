#requires webbpsf >=1.1.0

import glob
import pathlib

import numpy as np
import webbpsf
from astropy import time
from astropy.io import fits

nrc = webbpsf.NIRCam()

def makepsf(forimg,filt,savename,fov=10): #fov in arcsec
    f=fits.open(forimg)

    t=time.Time(f[0].header['MJD-AVG'],format='mjd')
    nrc.load_wss_opd_by_date(t.iso.replace(' ','T'))
    nrc.filter= filt

    pixscl=np.sqrt(abs(f[0].header['CDELT1']*f[0].header['CDELT2'])-abs(0))*60*60
    print(pixscl)

    psf= nrc.calc_psf(oversample=3)
    
    psf.writeto(savename,overwrite=True)


DATA_PATH = pathlib.Path("../../../Data/MAST_2023-12-03T1249/JWST")


if __name__ == "__main__":
    files = glob.glob(str(DATA_PATH / "*/*_sci.fits"))

    filters = ["f090w", "f150w", "f200w", "f277w", "f356w", "f444w"]

    for file, wfilter in zip(files, filters):
        print(file)
        makepsf(file, wfilter, f'../../PSFs/webbpsf/webb_psf_{wfilter}.fits')