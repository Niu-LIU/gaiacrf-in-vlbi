#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: generate-src-file.py
"""
Created on Tue Aug 13 14:02:03 2019

@author: Neo(liuniu@smail.nju.edu.cn)

This generate the .src file used as the a priori file of source positions in Solve.
The Gaia DR2 optical/ICRF3 radio positions for AGN will be used.


"""

from astropy.table import Table, join, Column
from astropy import units as u
import astropy.coordinates as coord
from astropy.coordinates import SkyCoord
import numpy as np
import matplotlib.pyplot as plt

# My modules
from my_progs.catalog.read_gaia import read_dr2_iers
from my_progs.catalog.read_icrf import read_icrf3
from my_progs.catalog.pos_diff import pos_diff_calc
from write_sou_src import write_sou_src, write_nnr_list

# -----------------------------  FUNCTIONS -----------------------------
# --------------------------------- MAIN --------------------------------

# Read ICRF3 S/X catalog
icrf3 = read_icrf3(wv="sx")

# Read Gaia DR2 IERS quasar data
gaiadr2 = read_dr2_iers()

#################################
# Look at this part later (begin)
#################################
comsou = join(icrf3, gaiadr2, keys="iers_name", table_names=["icrf3sx", "gaiadr2"])


[dRA, dDC, dRAerr, dDCerr, dRA_dDC_cov, ang_sep, Xa, Xd,
 X] = pos_diff_calc(comsou["ra_icrf3sx"], comsou["ra_err_icrf3sx"],
                    comsou["dec_icrf3sx"], comsou["dec_err_icrf3sx"],
                    comsou["ra_dec_corr_icrf3sx"], comsou["ra_gaiadr2"],
                    comsou["ra_err_gaiadr2"], comsou["dec_gaiadr2"],
                    comsou["dec_err_gaiadr2"], comsou["ra_dec_corr_gaiadr2"])

comsou.add_columns(
    [dRA, dDC, dRAerr, dDCerr, dRA_dDC_cov, ang_sep, Xa, Xd, X],
    names=[
        "dra", "ddec", "dra_err", "ddec_err", "dra_ddec_cov", "ang_sep",
        "nor_dra", "nor_ddec", "nor_sep"
    ])

comsou["dra"].unit = u.mas
comsou["ddec"].unit = u.mas
comsou["dra_err"].unit = u.mas
#################################
# Look at this part later (end)
#################################

# Use the ICRF3 defining sources in the Gaia DR2 dataset as the NNR list
maskdef = (comsou["type"] == "D")
comdef = comsou[maskdef]
souno = len(comdef)

print("There are {} among so-called ICRF3-defining sources in the Gaia DR2".format(souno))

comdef.rename_column("iers_name", "source_name")

# Write source list into a text file
deflist = "../logs/icrf3-def-in-gdr2.list"
print("Output file:", deflist)
lsthead = "*-- {} among ICRF3 defining sources from Gaia DR2".format(souno)
write_nnr_list(comdef["source_name"], lsthead, deflist)

# --------------------------------- END --------------------------------
