#!/usr/bin/env sh
# 目前还不清楚为什么--gres=gpu:8 --ntasks=1 --ntasks-per-node=1 就可以，
# 而--gres=gpu:8 --ntasks=8 --ntasks-per-node=8 就会报CUDA out of memory 的错 
mkdir -p log
now=$(date +"%Y%m%d_%H%M%S")
srun \
--partition=AD_Fusion \
--job-name=YOLO6D \
--gres=gpu:8 \
--ntasks=1 \
--ntasks-per-node=1 \
--cpus-per-task=5 \
--kill-on-bad-exit=1 \
--nodelist=SH-IDC1-10-5-36-217 \
--exclude=SH-IDC1-10-5-36-[51,57,61,93,166,176,181,182,188,191,208,214,216,238,239] \
python -u train_beer.py \
2>&1|tee log/$now.log