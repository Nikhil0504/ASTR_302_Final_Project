import pathlib
from astropy.table import Table
import numpy as np
from astropy.io import fits

class CatalogProcessor:
    def __init__(self, directory, detection_filter, output_path, sn=5.):
        self.directory = directory
        self.detection_filter = detection_filter
        self.output_path = pathlib.Path(output_path).resolve()
        self.catalogs = {}
        self.detection_cat = None
        self.master_table = None
        self._aperture_col = 'MAG_APER'
        self._aperture_col_err = 'MAGERR_APER'
        self.sn = sn
    
    def set_aperture_col(self, col, col_err):
        self._aperture_col = col
        self._aperture_col_err = col_err

    def get_catalog_paths(self):
        cat_paths = sorted(pathlib.Path(self.directory).resolve().glob('*.cat'))
        self.catalogs = {path.stem.upper(): path for path in cat_paths}

    def load_detection_catalog(self):
        if detection_path := self.catalogs.get(self.detection_filter):
            self.detection_cat = Table.read(detection_path, format='ascii.sextractor')

    def create_master_table(self):
        self.master_table = Table()

        self.master_table['id'] = self.detection_cat['NUMBER']
        self.master_table['ra'] = self.detection_cat['ALPHA_J2000']
        self.master_table['dec'] = self.detection_cat['DELTA_J2000']

        # q_iso = self.detection_cat['FLUX_AUTO'] / self.detection_cat['FLUX_ISO']
        f_auto, _ = self.convert_to_microjansky(self.detection_cat['MAG_AUTO'], self.detection_cat['MAGERR_AUTO'])
        f_aper, _ = self.convert_to_microjansky(self.detection_cat[self._aperture_col], self.detection_cat[self._aperture_col_err])

        q_iso = f_auto / f_aper

        for filter_name, path in self.catalogs.items():
            cat = Table.read(path, format='ascii.sextractor')

            # fit_header = fits.getheader(f'../../Data/plckg191/Images/anton/20230718_ProCessed/30mas/drz/mosaic_plckg191_nircam_{filter_name.lower()}_30mas_20230718_drz.fits')
            # pix_area = fit_header['PIXAR_SR']

            # do a sn cut if filter is F090W, F115W, F150W, F200W
            if filter_name in ['F090W', 'F115W', 'F150W', 'F200W']:
                detected_values, detected_errors = self.process_catalog(cat, q_iso, sn=self.sn, sn_cut=True)
            else:
                detected_values, detected_errors = self.process_catalog(cat, q_iso, sn=self.sn, sn_cut=True)
            
            # multiple with pix_area and 1e12 if values and errors are not -99
            # mask = np.logical_not(np.equal(detected_values, -99))
            # detected_values[mask] *= pix_area * 1e12
            # detected_errors[mask] *= pix_area * 1e12

            self.master_table[f'{filter_name}'] = detected_values
            self.master_table[f'{filter_name}_ERROR'] = detected_errors


    def process_catalog(self, catalog, q_iso, sn=5., sn_cut=True, flag_thresh=3):
        # f = catalog['FLUX_ISO']
        # ef = catalog['FLUXERR_ISO']
        f, ef = self.convert_to_microjansky(catalog[self._aperture_col], catalog[self._aperture_col_err])
        flags = catalog['FLAGS']

        nondetections = np.less_equal(f, 0) * np.greater(ef, 0)
        nonobservations = np.less_equal(ef, 0)

        f = np.clip(f, 1e-100, 1e10)
        ef = np.clip(ef, 1e-100, 1e10)

        nonobservations += np.equal(ef, 1e10)

        if sn_cut:
            nondetections += np.less_equal(f / ef, sn)
        
        flag_thresh_cutout = np.greater(flags, flag_thresh)
    
        detected = np.logical_not(nondetections + nonobservations + flag_thresh_cutout)
        
        fluxes, flux_errors = self.convert_to_microjansky(catalog[self._aperture_col], catalog[self._aperture_col_err])

        # detected_values = np.where(detected, q_iso * catalog['FLUX_ISO'], -99)
        # detected_errors = np.where(detected, q_iso * catalog['FLUXERR_ISO'], -99)

        detected_values = np.where(detected, q_iso * fluxes, -99)
        detected_errors = np.where(detected, q_iso * flux_errors, -99)

        # make all the flag_thresh_cutout values 0
        detected_values[flag_thresh_cutout] = 0
        detected_errors[flag_thresh_cutout] = 0

        return detected_values, detected_errors

    def convert_to_microjansky(self, values, errors):
        flux = 10**(-0.4*(values+48.6))*1e-7*1e4*1e26*1e6
        flux_err = (np.log(10.)/2.5)*errors*flux

        return flux, flux_err

    def save_master_table(self):
        if self.master_table is not None:
            self.master_table.write(self.output_path, 
                                    format='ascii.fixed_width_two_line', 
                                    delimiter=' ', 
                                    overwrite=True)
        else:
            raise ValueError('Master table not created yet.')

    def process_catalogs(self):
        self.get_catalog_paths()
        self.load_detection_catalog()
        self.create_master_table()
        self.save_master_table()
    
    def get_sn_table(self, save=True):
        sn_table = Table()

        sn_table['id'] = self.detection_cat['NUMBER']
        sn_table['ra'] = self.detection_cat['ALPHA_J2000']
        sn_table['dec'] = self.detection_cat['DELTA_J2000']

        for filter_name, path in self.catalogs.items():
            cat = Table.read(path, format='ascii.sextractor')

            f, ef = self.convert_to_microjansky(cat[self._aperture_col], cat[self._aperture_col_err])

            f = np.clip(f, 1e-100, 1e10)
            ef = np.clip(ef, 1e-100, 1e10)

            sn_table[f'{filter_name}_SN'] = f / ef

        if save:
            # output path + '_sn.cat'
            sn_table.write(
                self.output_path.parent / f'{self.output_path.stem}_sn.cat',
                format='ascii.fixed_width_two_line',
                delimiter=' ',
                overwrite=True,
            )
        return sn_table

# Example usage
processor = CatalogProcessor('../../sextractor/F444W/', 'F444W', '../../catalogs/master_catalog_f444w_astropy.cat', sn=2.)
processor.set_aperture_col('MAG_APER_1', 'MAGERR_APER_1')
processor.process_catalogs()
processor.get_sn_table()
