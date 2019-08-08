#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: write_sou_solve.py
"""
Created on Thu Apr 26 17:43:41 2018

@author: Neo(liuniu@smail.nju.edu.cn)
"""

import numpy as np
from write_solvesrc import write_solvesrc, write_NNRS
# from find_icrf2def import find_icrf2def
from souname_xmatch import read_soun
from read_gaiadr2 import read_gaiadr2_ascii


# -----------------------------  FUNCTIONS -----------------------------
def write_icrf2_solve(datafile, Gaiasouivs, fout):
    souivs = np.genfromtxt(
        datafile, usecols=(1,), dtype=str, unpack=True)

    RAh, RAm, DCd, DCm = np.genfromtxt(datafile,
                                       usecols=(4, 5, 7, 8),
                                       dtype=str,
                                       unpack=True)
    RAs, DCs, DC_erras = np.genfromtxt(datafile,
                                       usecols=(6, 9, 11),
                                       unpack=True)
    # as -> mas
    DC_err = DC_erras * 1.e3
    x = 0

    linefmt = "    %8s  %2s %2s %11.8f   %3s %2s  %10.7f   %7.3f   %s"

    for (souni, RAhi, RAmi, RAsi, DCdi, DCmi, DCsi, DC_erri
         ) in zip(souivs, RAh, RAm, RAs, DCd, DCm, DCs, DC_err):

        if souni not in Gaiasouivs:
            print(linefmt % (souni, RAhi, RAmi, RAsi,
                             DCdi, DCmi, DCsi, DC_erri, 'icrf2'),
                  file=fout)
        else:
            x += 1


def soudesign_trans(dsg1_sou, dsg1_all, dsg2_all):
    '''source designation1 -> source designation2
    e.g. ICRF designation -> IVS designation.
    '''

    deg2_sou = np.empty_like(dsg1_sou)
    # deg2_sou = []

    for i, sou in enumerate(dsg1_sou):
        if sou in dsg1_all:
            deg2_sou[i] = dsg2_all[dsg1_all == sou][0]
            # deg2_sou.append(dsg2_all[dsg1_all == sou][0])
        else:
            print("# Couldn't find the counterpart of %s" % sou)
            deg2_sou[i] = ' '
            # exit()

    # print("# ICRF designation -> IVS designation: OK")
    # deg2_sou = np.asarray(deg2_sou)

    return deg2_sou

# --------------------------------- END --------------------------------
