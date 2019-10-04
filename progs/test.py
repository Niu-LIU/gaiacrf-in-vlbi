# My modules
from my_progs.catalog.vsh_deg1_cor import vsh_deg01_fitting

# Transform columns into np.array


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
      (dra.size,
       par[3], sig[3], par[4], sig[4], par[5], sig[5],
       par[0], sig[0], par[1], sig[1], par[2], sig[2],))


print(" %+4.0f %3.0f  %+4.0f %3.0f  %+4.0f %3.0f"
      " %+4.0f %3.0f  %+4.0f %3.0f  %+4.0f %3.0f" %
      (par1[3], sig1[3], par1[4], sig1[4], par1[5], sig1[5],
       par1[0], sig1[0], par1[1], sig1[1], par1[2], sig1[2],
       par2[3], sig2[3], par2[4], sig2[4], par2[5], sig2[5],
       par2[0], sig2[0], par2[1], sig2[1], par2[2], sig2[2],
       par3[3], sig3[3], par3[4], sig3[4], par3[5], sig3[5],
       par3[0], sig3[0], par3[1], sig3[1], par3[2], sig3[2]))
