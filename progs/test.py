comsou = join(k2sx, xka2sx, keys=["iers_name"], table_names=["k", "xka"])
comsou = join(comsou, opt2sx, keys=["iers_name"])

# Rename some columns
comsou.rename_columns(['dra', 'ddec', 'dra_err', 'ddec_err', 'dra_ddec_cov',
                       'ang_sep', 'nor_ra', 'nor_dec', 'nor_sep'],
                      ['dra_opt', 'ddec_opt', 'dra_err_opt', 'ddec_err_opt',
                       'dra_ddec_cov_opt',
                       'ang_sep_opt', 'nor_ra_opt', 'nor_dec_opt', 'nor_sep_opt'])
