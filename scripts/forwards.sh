#!/bin/bash

cd $(dirname $0)/..

bash self_training/scripts/train.methodius.lstm.shuf.lbl.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.lbl.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.lbl.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.ft.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.ft.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.itr2.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.itr2.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.itr2.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.ft.itr2.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.ft.itr2.sh 1c;
echo 'DONE with vanila self training phase and generation';
