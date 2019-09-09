# My modules
from my_progs.catalog.vsh_deg1_cor import vsh_deg01_fitting

# Gaia DR2 - ICRF3 S/X
pmra = np.array(defsou["pmra"])
pmdec = np.array(defsou["pmdec"])
pmraerr = np.array(defsou["pmra_err"])
pmdecerr = np.array(defsou["pmdec_err"])
pmradeccov = np.array(defsou["pmra_err"] * defsou["pmdec_err"] * defsou["pmra_pmdec_corr"])

# Transformation parameters
# l_max = 2
par, sig, _, _, _, _ = vsh_deg01_fitting(
    pmra, pmdec, rarad, decrad, pmraerr, pmdecerr,
    cov=pmradeccov, elim_flag="None")

# mas -> uas
spin = par * 1.e3
serr = sig * 1.e3

# Print results
print("Estimates (%6d sources)\n"
      "----------------------------------------------"
      "----------------------------------------------\n"
      "                 Rotation [uas]                  "
      "                 Glide [uas]               \n"
      "             x             y             z"
      "             x             y             z\n"
      "----------------------------------------------"
      "----------------------------------------------\n"
      "        %+4.0f +/- %3.0f  %+4.0f +/- %3.0f  %+4.0f +/- %3.0f"
      "        %+4.0f +/- %3.0f  %+4.0f +/- %3.0f  %+4.0f +/- %3.0f\n"
      "----------------------------------------------"
      "----------------------------------------------\n" %
      (pmra.size,
       spin[3], serr[3], spin[4], serr[4], spin[5], serr[5],
       spin[0], serr[0], spin[1], serr[1], spin[2], serr[2],))
