# Neural Methodius

This repo provides data and scripts used in the paper **Neural NLG for Methodius: From RST Meaning Representations to Texts**
by Symon Jory Stevens-Guille, Aleksandre Maskharashvili, Amy Isard, Xintong Li and Michael White, published at INLG2020.

## Reference

Bibtex will be available soon.

## Datasets

There are four datasets:
- data/RST-SM-data
- data/FACT-SM-data
- data/RST-LG-data
- data/FACT-LG-data

## Code

The code is tested on commit `3822db3` of [fairseq](https://github.com/pytorch/fairseq).

## Data Preperation Steps and Training

### Pre-Processing data


By default, in the "data" there are the datasets used in our experiments, "RST-SM-data", "FACT-SM-data", "RST-LG-data", and "FACT-LG-data", where SM indicates that the folder contains a small self-training dataset "train.augment-del.mr" (around 950 sources), whereas LG means that the folder contains a large self-training dataset (around 80K sources). 


To use either of these datasets from the folder "data", rename that dataset (e.g. "RST-SM-data") as "methodius".

Then, run the command:     

<code> bash scripts/prep_tsv.sh methodius </code>


### Preparing data for self-training

Before trainig, one needs to preprocess data for self-training and reverse model. These are the following steps.

To preprocess the data, use: 
- For SM data:       	     <code> bash scripts/prep_sm.sh </code>

- For LG data:       	     <code> bash scripts/prep_lg.sh </code>

(In the case of SM data, it will randomly select 250 sources for valid out of 950 of the "train.augment-del.mr" 
file and the rest for training, whereas in the case of LG, it will select 3000 out of 80K).


### Training

To train vanilla self training use:

- For vanilla self-training:  

<code> bash forwards.sh </code>

- For reverse model reranking with self-training: 

<code> bash reverseds.sh </code>


N.B. One may run both of the scripts <code> bash forwards.sh </code> and <code> bash reverseds.sh </code> silmulteniously.

### Generated files
After the training step, under the folder "self_training/checkpoints/methodius/pct-1c/" could be found generated files ("gen.txt" and "challengetestgen.txt", which can be found by running the command <code>  find . -iname "*gen.txt" </code> in the folder "self_training/checkpoints/methodius".)

## Acknowledgement

The code is developed from [znculee/TreeNLG](https://github.com/znculee/TreeNLG).
