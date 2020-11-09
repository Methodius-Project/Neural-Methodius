#!/bin/bash

cd $(dirname $0)/..

bash self_training/scripts/train.methodius.lstm.shuf.lbl.rev.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.rrk-rev.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.rrk-rev.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.rrk-rev.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.ft.rrk-rev.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.ft.rrk-rev.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.rrk-rev.rev.sh;
bash self_training/scripts/train.methodius.lstm.shuf.ft.rrk-rev.rev.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.rrk-rev.itr2.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.rrk-rev.itr2.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.rrk-rev.itr2.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.ft.rrk-rev.itr2.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.ft.rrk-rev.itr2.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.rrk-rev.rev.itr2.sh;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.rrk-rev.rev.itr2.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.rrk-rev.rev.itr2.sh 1c;
bash self_training/scripts/prepare.methodius.shuf.plbl.rrk-rev.itr3.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.plbl.rrk-rev.itr3.sh 1c;
bash self_training/scripts/train.methodius.lstm.shuf.ft.rrk-rev.itr3.sh 1c;
bash self_training/scripts/generate.methodius.lstm.shuf.ft.rrk-rev.itr3.sh 1c;
bash self_training/scripts/chgenerate.methodius.lstm.shuf.ft.rrk-rev.itr3.sh 1c;
echo 'DONE reverse model reranking with self training and generating.';
