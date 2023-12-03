import pathlib

from astropy.io import fits

DATA_PATH = pathlib.Path("../../../Data/MAST_2023-12-03T1249/JWST")


def isolate_images(path, save_sci=True, save_wht=True):
    """Isolate SCI and WHT images from i2d files.

    Parameters
    ----------
    path : str
        Path to i2d file.
    save_sci : bool
        Whether to save the SCI image.
    save_wht : bool
        Whether to save the WHT image.
    """
    hdu = fits.open(path)

    # For i2d files, SCI image is 1 and WHT is 4
    sci = hdu[1].data
    wht = hdu[4].data
    header = hdu[1].header

    if save_sci:
        fits.writeto(path.parent / f"{path.stem}_sci.fits", sci, header, overwrite=True)
    if save_wht:
        fits.writeto(path.parent / f"{path.stem}_wht.fits", wht, header, overwrite=True)


if __name__ == "__main__":
    filters = ["f090w", "f150w", "f200w", "f277w", "f356w", "f444w"]

    for filter in filters:
        print("Isolating images for filter", filter)
        isolate_images(
            DATA_PATH
            / f"jw04446-c1000_t009_nircam_clear-{filter}/jw04446-c1000_t009_nircam_clear-{filter}_i2d.fits"
        )
