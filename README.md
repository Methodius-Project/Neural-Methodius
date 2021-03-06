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

```bash
bash scripts/prep_tsv.sh methodius
```


### Preparing data for self-training

Before trainig, one needs to preprocess data for self-training and reverse model.
These are the following steps.

To preprocess the data, use:
- For SM data: `bash scripts/prep_sm.sh`

- For LG data: `bash scripts/prep_lg.sh`

(In the case of SM data, it will randomly select 250 sources for valid out of 950 of the "train.augment-del.mr"
file and the rest for training, whereas in the case of LG, it will select 3000 out of 80K).


### Training

To train vanilla self training use:

- For vanilla self-training:

```bash
bash forwards.sh
```

- For reverse model reranking with self-training:

```bash
bash reverseds.sh
```

N.B. One may run both of the scripts `bash forwards.sh` and `bash reverseds.sh` silmulteniously.

### Generated files

After the training step, under the folder `self_training/checkpoints/methodius/pct-1c/` could be found generated files (`gen.txt` and `challengetestgen.txt`, which can be found by running the command `find . -iname "*gen.txt"` in the folder `self_training/checkpoints/methodius`.)

## Measures of performance
To find repetitions, omissions, and hallucinations (in `gen.txt`), you may run the following command:
```bash
python scripts/relCountRoh_measure.py gen.txt
```

To find how many relations a model generated correctly/incorrectly, you may run the following command:
```bash
python scripts/relCountRoh_measure.py gen.txt relcount
```


## Acknowledgement

The code is developed from [znculee/TreeNLG](https://github.com/znculee/TreeNLG).
