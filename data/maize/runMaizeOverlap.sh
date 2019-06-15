#!/bin/bash

#parallel --gnu -j 8 --delay 60 --progress \
#camoco --debug overlap \
#--gwas {2} \
#--snp2gene strongest \
#--strongest-attr numIterations \
#--strongest-higher \
#--candidate-window-size {4} \
#--candidate-flank-limit {5} \
#--out GWAS/{2}/FDR/{2}_{1}_{3}_{4}_{5}.csv \
#{1} \
#{3} \
#::: ZmRoot ZmSAM ZmPAN \
#::: ZmIonome \
#::: locality density \
#::: 10000 20000 50000 100000 500000 \
#::: 1 2 5

parallel --gnu -j 8 --delay 60 --progress \
camoco --debug overlap \
--gwas {2} \
--snp2gene strongest \
--strongest-attr rmip \
--strongest-higher \
--candidate-window-size {4} \
--candidate-flank-limit {5} \
--out GWAS/{2}/FDR/{2}_{1}_{3}_{4}_{5}.csv \
{1} \
{3} \
::: ZmRoot ZmSAM ZmPAN \
::: ZmWallace \
::: locality density \
::: 10000 20000 50000 100000 500000 \
::: 1 2 5

