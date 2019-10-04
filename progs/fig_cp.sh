#!/bin/bash
#########################################################################
# File Name: fig_cp.sh
# Author: Neo
# mail: liuniu@smail.nju.edu.cn
# Created Time: Fri Mar 29 21:12:39 2019
#########################################################################

fig_list=('gcrf250-allsky-dist.eps' \
          'gcrf250-separation.eps' \
          'gcrf250-pos-diff.eps' \
          'gcrf250-cat-diff-on-ra.eps' \
          'gcrf250-cat-diff-on-dec.eps' \
          'opa2019a-fix-cat-diff-on-ra.eps' \
          'opa2019a-fix-cat-diff-on-dec.eps' \
          'dec_err_250.eps' \
          'vsh-deg01-to-gdr2.eps' \
          'gcrf250-eop-diff.eps' \
          'opa2019a-250-eop-diff.eps' \
          'opa2019a-fix-eop-diff.eps' \
          'gcrf250-wgt-eop-diff.eps' \
          'opa2019a-wgt-eop-diff.eps')

out_dir="../notes/figs/"

for fig in ${fig_list[@]};
do
	cp ../plots/${fig} ${out_dir}
    echo "copy ${fig}: Done!"
done
