#!/bin/bash

cd $(dirname $0)/../..

export CUDA_VISIBLE_DEVICES=$2
TMPDIR=/tmp
data=methodius
model=lstm
pct=pct-$1
trn=shuf.lbl
SAVEDIR=self_training/checkpoints/$data/$pct/$trn.$model
testpfx=challengetest

ln -s $(readlink -f data-prep/$data/$testpfx.mr-ar.ar) self_training/data-prep/$data/$pct/$trn/$testpfx.mr-ar.ar
ln -s $(readlink -f data-prep/$data/$testpfx.mr-ar.mr) self_training/data-prep/$data/$pct/$trn/$testpfx.mr-ar.mr


gen=challengetestgen.txt
fairseq-generate self_training/data-prep/$data/$pct/$trn \
  --user-dir . \
  --gen-subset $testpfx \
  --path $SAVEDIR/checkpoint_best.pt \
  --dataset-impl raw \
  --max-sentences 128 \
  --beam 5 \
  --max-len-a 2 --max-len-b 50 \
  > $SAVEDIR/$gen
bash scripts/measure_scores.sh $SAVEDIR/$gen self_training/data-prep/$data/$pct/$trn/$testpfx.mr-ar.ar
