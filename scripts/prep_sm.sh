#!/bin/bash

cd $(dirname $0)/..

bash self_training/scripts/prepare.methodius_sm.ulbl.sh;
bash self_training/scripts/prepare.methodius.shuf.lbl.sh;
bash self_training/scripts/prepare.methodius.shuf.lbl.rev.sh;
