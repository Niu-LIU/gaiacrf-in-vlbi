#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name: write_sou_src.py
"""
Created on Thu Apr 26 17:43:41 2018

@author: Neo(liuniu@smail.nju.edu.cn)

Sep 06, 2019: change the colomun name from "dec_err" to "wgt_err"

"""

from astropy.coordinates import Angle
import astropy.units as u
import numpy as np
import sys

__all__ = ["write_sou_src", "write_nnr_list"]


# -----------------------------  FUNCTIONS -----------------------------
def write_sou_src(cat, ofile=None, header="", comments=""):
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
    if ofile is None:
        fout = sys.stdout
    else:
        try:
            fout = open(ofile, "w")
        except Exception as e:
            exit()

    # Print header information
    print(header, file=fout)

    # Format of every line
    if len(comments):
        linefmt = "%8s     %02d %02d %11.8f    %s %02d %10.7f  %7.3f  ! %s"
    else:
        linefmt = "%8s     %02d %02d %11.8f    %s %02d %10.7f  %7.3f"

    # Loop to write the position for every source
    for i in range(len(cat)):
        souname = cat[i]["source_name"]
        ra, dec = cat[i]["ra"], cat[i]["dec"]
        wgt_err = cat[i]["wgt_err"]

        raang = Angle(ra * u.deg)
        decang = Angle(dec * u.deg)
        rah, ram, ras = raang.hms
        decd, decm, decs = decang.dms

        # When converting an Angle object into degrees using dms method,
        # the degree, arcminute, and arcsecond extracted from the resulted tuple
        # would be all negative if the Angle is negative.
        # But we only want the degree part to be negative.
        if dec < 0 and decd == 0:
            decdstr = "-00"
        else:
            decdstr = "{:+03.0f}".format(decd)

        decm, decs = np.fabs(decm), np.fabs(decs)

        if len(comments):
            print(linefmt % (souname, rah, ram, ras, decdstr, decm, decs, wgt_err,
                             comments), file=fout)
        else:
            print(linefmt % (souname, rah, ram, ras, decdstr, decm, decs, wgt_err), file=fout)

    # Close the file
    if fout is not sys.stdout:
        fout.close()


def write_nnr_list(soulist, header="", ofile=None):
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

    # print header
    print("*----", file=fout)
    print(header, file=fout)
    print("*----", file=fout)

    # Loop to write
    print("    ", file=fout, end="")
    for i, sou in enumerate(soulist):
        print("{:8}  ".format(sou), file=fout, end="")

        if not (i+1) % 8:
            print("\\\n    ", file=fout, end="")

    print("\n*----", file=fout)

    # Close the file
    if fout is not sys.stdout:
        fout.close()


if __name__ == "__main__":
    print("This is a file only containing some ")

# --------------------------------- END --------------------------------
