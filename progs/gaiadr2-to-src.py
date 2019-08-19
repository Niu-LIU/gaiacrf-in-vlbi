#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: Gaiadr22Solve.py
"""
Created on Thu Apr 26 17:43:09 2018

@author: Neo(liuniu@smail.nju.edu.cn)
"""

from astropy.table import Table
import numpy as np
import os

# My modules
from write_sou_src import write_sou_src, write_nnr_list


# -----------------------------  FUNCTIONS -----------------------------
def read_dr2_qso(gdr2file):
    """Read the positional information of Gaia DR2 auxiliary IERS catalog.
    """

    # Read Gaia DR2 IERS quasar data
    gdr2 = Table.read(gdr2file)

    # Only the positional information are kept.
    gdr2.keep_columns(["iers_name",
                       "source_id",
                       "ra",
                       "ra_error",
                       "dec",
                       "dec_error",
                       "parallax",
                       "parallax_error",
                       "pmra",
                       "pmra_error",
                       "pmdec",
                       "pmdec_error",
                       "ra_dec_corr",
                       "ra_parallax_corr",
                       "ra_pmra_corr",
                       "ra_pmdec_corr",
                       "dec_parallax_corr",
                       "dec_pmra_corr",
                       "dec_pmdec_corr",
                       "parallax_pmra_corr",
                       "parallax_pmdec_corr",
                       "pmra_pmdec_corr",
                       "phot_g_mean_mag",
                       "phot_bp_mean_mag",
                       "phot_rp_mean_mag"])

    # Rename the column names
    gdr2.rename_column("ra_error", "ra_err")
    gdr2.rename_column("dec_error", "dec_err")
    gdr2.rename_column("parallax_error", "parallax_err")
    gdr2.rename_column("pmra_error", "pmra_err")
    gdr2.rename_column("pmdec_error", "pmdec_err")

    return gdr2


# -------------------------------  MAIN -------------------------------
'''Write the Gaia DR1 source position into the Solve format.
'''

print("======================= BEGIN ============================\n"
      "# Write Gaia DR2 aux_iers_cross_id into Solve format")


# Input &output files
ifile = "../data/gaiadr2-aux-iers.fits"
srcfile = "../logs/gaiadr2-aux-iers.src"
srclist = "../logs/gaiadr2-aux-iers.list"

print("Original file:", ifile)
print("Outpuf src file:", srcfile)
print("output list file:", srclist)

# header
srchead = ("$$ This file consists of SOLVE-format positions for 2820 "
           "sources from GaiaDR2_IERS.\n$$ original file: {}".format(ifile))
lsthead = "*-- 2820 optical counterparts of ICRF sources from Gaia DR2"


gdr2 = read_dr2_qso(ifile)
gdr2.rename_column("iers_name", "source_name")


write_sou_src(gdr2, srcfile, srchead, "GaiaDR2_IERS")
write_nnr_list(gdr2["source_name"], lsthead, srclist)

# Copy files
datadir = "/home/neo/data/solutions/gaia-crf/"
print("Copy", srcfile, "to", datadir)
os.system("cp {} {}".format(srcfile, datadir))
print("Copy", srclist, "to", datadir)
os.system("cp {} {}".format(srclist, datadir))

print('=======================  END  ============================')

# --------------------------------- END --------------------------------
