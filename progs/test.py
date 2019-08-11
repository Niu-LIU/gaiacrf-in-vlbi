from astropy.table import Table, Column
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
import sys

# My modules
from my_progs.catalog.pos_err import pos_err_calc

def read_icrf3(icrf3_file="../data/icrf3sx.txt"):
    """Read the ICRF3 catalog.

    Parameter
    ---------
    icrf3_file : string
        file name and path of the ICRF3 catalog
    wv : string
        wavelength, could be "sx", "k", or "xka".

    Return
    ------
    icrf3 : an astropy.Table object
        data in the catalog
    """

    icrf3 = Table.read(icrf3_file,
                       format="ascii.fixed_width", data_start=16,
                       names=["icrf_name", "iers_name", "type",
                              "ra_err", "dec_err", "ra_dec_corr",
                              "mean_obs", "beg_obs", "end_obs",
                              "nb_sess", "nb_del"],
                       col_starts=[5, 25, 35, 83, 98,
                                   108, 118, 127, 136, 145, 150],
                       col_ends=[20, 32, 35, 92, 106,
                                 114, 124, 133, 142, 148, 155])

    # Position information
    ra_dec_str = Table.read(icrf3_file,
                            format="ascii.fixed_width", data_start=16,
                            names=["ra_dec"], col_starts=[40], col_ends=[77])


    ra_dec = SkyCoord(ra_dec_str["ra_dec"], unit=(u.hourangle, u.deg))
    ra = Column(ra_dec.ra, name="ra")
    dec = Column(ra_dec.dec, name="dec")

    # Add source position to the table
    icrf3.add_columns([ra, dec], indexes=[3, 3])

    # Add unit information
    icrf3["ra_err"] = icrf3["ra_err"] * 15e3 * np.cos(ra_dec.dec.rad)
    icrf3["ra_err"].unit = u.mas
    icrf3["dec_err"].unit = u.arcsec
    icrf3["dec_err"] = icrf3["dec_err"].to(u.mas)

    # Calculate the semi-major axis of error ellipse
    pos_err = pos_err_calc(
        icrf3["ra_err"], icrf3["dec_err"], icrf3["ra_dec_corr"])

    # Add the semi-major axis of error ellipse to the table
    icrf3.add_column(pos_err, name="pos_err", index=9)

    return icrf3

if __name__ == '__main__':
    read_icrf3()
