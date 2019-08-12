# icrf2-nga-09 - gaia dr2
gli1 = w21[:3]
rot1 = w21[3:6]
qua1 = w21[6:]

gerr1 = sig21[:3]
rerr1 = sig21[3:6]
qerr1 = sig21[6:]

glimod1, glierr1 = vec_mod_calc(gli1, gerr1)
rotmod1, roterr1 = vec_mod_calc(rot1, rerr1)

# icrf2-ga-09 - gaia dr2
gli2 = w22[:3]
rot2 = w22[3:6]
qua2 = w22[6:]

gerr2 = sig22[:3]
rerr2 = sig22[3:6]
qerr2 = sig22[6:]

glimod2, glierr2 = vec_mod_calc(gli2, gerr2)
rotmod2, roterr2 = vec_mod_calc(rot2, rerr2)
