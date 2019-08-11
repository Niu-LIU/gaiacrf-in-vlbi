#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: write_sou_solve.py
"""
Created on Thu Apr 26 17:43:41 2018

@author: Neo(liuniu@smail.nju.edu.cn)
"""

from astropy.coordinates import Angle
import astropy.units as u
import numpy as np

__all__ = ["write_solve_src", "write_nnr_list"]



# -----------------------------  FUNCTIONS -----------------------------
def write_solve_src(cat, ofile, comments=""):
    """Write source position into .src format

    Parameters
    ----------
    cat: astropy.table.Table object
        catalog
    ofile: string
        output file name
    comments: string
        add comments to the end of each line

    Return
    ------
    None
    """

    # Open the file
    fout = open(ofile, "w")

    # Format of every line
    linefmt = "    %8s  %2s %2s %11.8f   %3s %2s  %10.7f   %7.3f   %s"


    # Loop to write the position for every source
    for i in range(len(cat)):
        souname = cat[i]["source_name"]
        ra, dec = cat[i]["ra"], cat[i]["dec"]
        dec_err = cat[i]["dec_err"]

        raang, decang = Angle(ra*u.deg), Angle(dec*u.deg)
        rah, ram, ras = raang.hms
        decd, decm, decs = decang.hms

        print(linefmt % (souname, rah, ram, ras, decd, decm, decs, dec_err,
          comments), file=fout)

    # Close the file
    fout.close()



def write_nnr_list():


if __name__ == "__main__":
  print("This is a file only containing some ")

# --------------------------------- END --------------------------------
