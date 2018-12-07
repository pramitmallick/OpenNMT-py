#!/bin/sh
#
#SBATCH --verbose
#SBATCH --job-name=test2
#SBATCH --time=100:00:00
#SBATCH --nodes=1
#SBATCH --mem=50GB
###SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1

module load python/intel/2.7.12 pytorch/0.2.0_1 
module load torchvision/0.1.8
python train.py -data data/iwslt15 -save_model iwslt-model -input_feed 0 -encoder_type brnn -global_attention mlp -learning_rate 1 -learning_rate_decay 0.25 -gpu_ranks 0
 
