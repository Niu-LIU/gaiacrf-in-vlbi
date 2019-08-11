#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: read_icrfn.py
"""
Created on Sat Sep 29 18:15:50 2018

@author: Neo(liuniu@smail.nju.edu.cn)
"""

from astropy.table import Table, Column
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
import sys

# My modules
from my_progs.catalog.pos_err import pos_err_calc

__all__ = ["read_icrf2", "read_icrf3"]


# -----------------------------  FUNCTIONS -----------------------------
def read_icrf2_old(icrf2_file="../data/icrf2.dat"):
    """Read the ICRF2 catalog.

    Parameter
    ---------
    icrf32_file : string
        file name and path of the ICRF2 catalog

    Return
    ------
    icrf2 : an astropy.Table object
        data in the catalog
    """

    # Read ICRF2 catalog
    icrf2 = Table.read(icrf2_file,
                       format="ascii.fixed_width_no_header",
                       names=["icrf_name", "ivs_name", "iers_name", "type",
                              "ra_err", "dec_err", "ra_dec_corr",
                              "mean_obs", "beg_obs", "end_obs",
                              "nb_sess", "nb_del"],
                       col_starts=[0, 17, 25, 35, 73, 84,
                                   94, 101, 109, 117, 125, 130],
                       col_ends=[15, 24, 33, 35, 82, 92,
                                 99, 107, 115, 123, 128, 135])

    # Position information
    ra_dec_str = Table.read(icrf2_file,
                            format="ascii.fixed_width_no_header",
                            data_start=17, names=["ra_dec"],
                            col_starts=[37], col_ends=[71])

    ra_dec = SkyCoord(ra_dec_str["ra_dec"], unit=(u.hourangle, u.deg))
    ra = Column(ra_dec.ra, name="ra")
    dec = Column(ra_dec.dec, name="dec")

    # Add source position to the table
    icrf2.add_columns([ra, dec], indexes=[3, 3])

    # Add unit information
    icrf2["ra_err"] = icrf2["ra_err"] * 15e3 * np.cos(ra_dec.dec.rad)
    icrf2["ra_err"].unit = u.mas
    icrf2["dec_err"].unit = u.arcsec
    icrf2["dec_err"] = icrf2["dec_err"].to(u.mas)

    # Calculate the semi-major axis of error ellipse
    pos_err = pos_err_calc(
        icrf2["ra_err"], icrf2["dec_err"], icrf2["ra_dec_corr"])

    # Add the semi-major axis of error ellipse to the table
    icrf2.add_column(pos_err, name="pos_err", index=9)
    icrf2["pos_err"].unit = u.mas

    return icrf2


def read_icrf2(icrf2_file="../data/icrf2-all.txt"):
    """Read the ICRF2 catalog.

    Parameter
    ---------
    icrf32_file : string
        file name and path of the ICRF2 catalog

    Return
    ------
    icrf2 : an astropy.Table object
        data in the catalog
    """

    # Read ICRF2 catalog
    icrf2 = Table.read(icrf2_file,
                       format="ascii.fixed_width_no_header", data_start=17,
                       names=["icrf_name", "iers_name", "type",
                              "ra_err", "dec_err", "ra_dec_corr",
                              "mean_obs", "beg_obs", "end_obs",
                              "nb_sess", "nb_del"],
                       col_starts=[5, 23, 33, 73, 84,
                                   96, 104, 112, 120, 130, 135],
                       col_ends=[21, 31, 34, 84, 94,
                                 102, 111, 119, 127, 134, 141])

    # Position information
    ra_dec_str = Table.read(icrf2_file,
                            format="ascii.fixed_width_no_header",
                            data_start=17, names=["ra_dec"],
                            col_starts=[36], col_ends=[72])

    ra_dec = SkyCoord(ra_dec_str["ra_dec"], unit=(u.hourangle, u.deg))
    ra = Column(ra_dec.ra, name="ra")
    dec = Column(ra_dec.dec, name="dec")

    # Add source position to the table
    icrf2.add_columns([ra, dec], indexes=[3, 3])

    # Add unit information
    icrf2["ra_err"] = icrf2["ra_err"] * 15e3 * np.cos(ra_dec.dec.rad)
    icrf2["ra_err"].unit = u.mas
    icrf2["dec_err"].unit = u.arcsec
    icrf2["dec_err"] = icrf2["dec_err"].to(u.mas)

    # Calculate the semi-major axis of error ellipse
    pos_err = pos_err_calc(
        icrf2["ra_err"], icrf2["dec_err"], icrf2["ra_dec_corr"])

    # Add the semi-major axis of error ellipse to the table
    icrf2.add_column(pos_err, name="pos_err", index=8)
    icrf2["pos_err"].unit = u.mas

    return icrf2


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

def write_nnr_list(soulist, ofile=None):
    """Write source list by every 8 sources per line

    Parameters
    ----------
    soulist: astropy.table.Table object
        source list
    ofile: string
        output file name

    Return
    ------
    None
    """

    # Open the file
    if ofile is None:
        fout = sys.stdout
    else:
        fout = open(ofile, "w")

    # Loop to write
    print("    ", file=fout, end="")
    for i, sou in enumerate(soulist):
        print("{:8}  ".format(sou), file=fout, end="")

        if not (i+1) % 8:
            print("\\\n    ", file=fout, end="")

    # Close the file
    if fout is not sys.stdout:
        fout.close()


# -------------------------------- MAIN --------------------------------
if __name__ == '__main__':
    pass
# --------------------------------- END --------------------------------
