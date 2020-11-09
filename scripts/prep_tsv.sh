#!/bin/bash

cd $(dirname $0)/..

src=mr
tgt=ar
datafolder=$1
prep=data-prep/$datafolder
orig=data/$datafolder

mkdir -p $prep

echo -e "show data sample...\n"
awk -F '\t' 'NR==1 {print $1,$2}' $orig/train.tsv ; echo ""
awk -F '\t' 'NR==1 {print $3}' $orig/train.tsv ; echo ""
awk -F '\t' 'NR==1 {print $4}' $orig/train.tsv ; echo ""
awk -F '\t' 'NR==1 {print $4}' $orig/train.tsv | \
  sed 's/\[\w\+//g' | sed 's/\]//g' | awk '{$1=$1;print}' ; echo ""

echo "creating train..."
awk -F '\t' '{print $1}' $orig/train.tsv > $prep/tmp.train.$src
awk -F '\t' '{print $2}' $orig/train.tsv > $prep/tmp.train.$tgt
echo "creating valid..."
awk -F '\t' '{print $1}' $orig/valid.tsv   > $prep/valid.$src-$tgt.$src
awk -F '\t' '{print $2}' $orig/valid.tsv   > $prep/valid.$src-$tgt.$tgt
echo "creating test..."
awk -F '\t' '{print $1}' $orig/test.tsv  > $prep/test.$src-$tgt.$src
awk -F '\t' '{print $2}' $orig/test.tsv  > $prep/test.$src-$tgt.$tgt
echo "creating challengetest..."
awk -F '\t' '{print $1}' $orig/challengetest.tsv  > $prep/challengetest.$src-$tgt.$src
awk -F '\t' '{print $2}' $orig/challengetest.tsv  > $prep/challengetest.$src-$tgt.$tgt
echo "copying train.augment-del.mr..."
cp $orig/train.augment-del.mr $prep/train.augment-del.mr

echo -e "\nproprecessing..."
fairseq-preprocess \
  --source-lang $src --target-lang $tgt \
  --trainpref $prep/tmp.train \
  --destdir $prep \
  --dataset-impl raw \

rm $prep/tmp.*
