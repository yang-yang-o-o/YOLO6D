#!/usr/bin/env sh
# 如果不加 --cpus-per-task=5 就会一直卡这执行慢，因为默认分配1个cpu

mkdir -p log
now=$(date +"%Y%m%d_%H%M%S")
srun \
--partition=AD_Fusion \
--gres=gpu:1 \
-n1 \
--ntasks-per-node=1 \
--cpus-per-task=5 \
--job-name=YOLO6D \
--kill-on-bad-exit=1 \
python test.py \
2>&1|tee log/tets-$now.log