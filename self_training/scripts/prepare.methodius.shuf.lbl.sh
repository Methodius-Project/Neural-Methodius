#!/bin/bash

cd $(dirname $0)/../..

data=methodius
src=mr
tgt=ar
orig=data-prep/$data
prep=self_training/data-prep/$data

mkdir -p $prep/pct-1c/shuf.lbl

build_vocab() {
  sed 's/ /\n/g' $1 | \
  awk '
    {if ($0!="") wc[$0]+=1}
    END {for (w in wc) print w, wc[w]}
  ' | \
  LC_ALL=C sort -k2,2nr -k1,1
}

combine_vocab() {
  awk '
    FNR==NR {wc[$1]=$2; next}
    {wc[$1]+=$2}
    END {for (w in wc) print w, wc[w]}
  ' $1 $2 | \
  LC_ALL=C sort -k2,2nr -k1,1
}

paste $orig/train.$src-$tgt.$src $orig/train.$src-$tgt.$tgt | shuf > $prep/train.shuf.$src-$tgt.tsv
awk -F '\t' '{print $1}' $prep/train.shuf.$src-$tgt.tsv > $prep/pct-1c/shuf.lbl/train.$src-$tgt.$src
awk -F '\t' '{print $2}' $prep/train.shuf.$src-$tgt.tsv > $prep/pct-1c/shuf.lbl/train.$src-$tgt.$tgt
rm $prep/train.shuf.$src-$tgt.tsv
paste $orig/valid.$src-$tgt.$src $orig/valid.$src-$tgt.$tgt | shuf > $prep/valid.shuf.$src-$tgt.tsv
awk -F '\t' '{print $1}' $prep/valid.shuf.$src-$tgt.tsv > $prep/pct-1c/shuf.lbl/valid.$src-$tgt.$src
awk -F '\t' '{print $2}' $prep/valid.shuf.$src-$tgt.tsv > $prep/pct-1c/shuf.lbl/valid.$src-$tgt.$tgt
rm $prep/valid.shuf.$src-$tgt.tsv

ln -s $(readlink -f $orig/dict.$src.txt) $prep/pct-1c/shuf.lbl/dict.$src.txt
ln -s $(readlink -f $orig/dict.$tgt.txt) $prep/pct-1c/shuf.lbl/dict.$tgt.txt
grep '^\[__\S*' $orig/dict.$tgt.txt | awk '{print $1}' > $prep/pct-1c/shuf.lbl/dict.nt.$tgt.txt

ln -s $(readlink -f $orig/test.$src-$tgt.$src) $prep/pct-1c/shuf.lbl/test.$src-$tgt.$src
ln -s $(readlink -f $orig/test.$src-$tgt.$tgt) $prep/pct-1c/shuf.lbl/test.$src-$tgt.$tgt

ln -s $(readlink -f $prep/ulbl/train.$src-$tgt.$src) $prep/pct-1c/shuf.lbl/train.ulbl.$src-$tgt.$src
ln -s $(readlink -f $prep/ulbl/valid.$src-$tgt.$src) $prep/pct-1c/shuf.lbl/valid.ulbl.$src-$tgt.$src

num_train=$(wc -l $prep/pct-1c/shuf.lbl/train.$src-$tgt.$src | cut -d ' ' -f 1)
num_valid=$(wc -l $prep/pct-1c/shuf.lbl/valid.$src-$tgt.$src | cut -d ' ' -f 1)






