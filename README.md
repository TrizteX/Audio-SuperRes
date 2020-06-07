# Audio Super Resolution for Improved Speech Recognition
A project to use audio super resolution to upsample english speech and feed to speech recognition softwares for better accuracy

The paper for audio super resolution: https://arxiv.org/pdf/1708.00853.pdf :AUDIO SUPER-RESOLUTION USING NEURAL NETS by Volodymyr Kuleshov, S. Zayd Enam, and Stefano Ermon

The code has been adapted from the following github repo:https://github.com/leekh7411/Fast-Audio-Super-Resolution
The network has been trained on the VCTK corpus as provided by University of Edinburgh: https://datashare.is.ed.ac.uk/handle/10283/2651

Major changes made to the repo are as follows:
=>All code has been ported to notebooks for easier runtime accessibility.
=>Dataset loading has been modified for the current structure of VCTK corpus.
=>Final predictions have been converted to audio files with the intended sampling rates for qualitative and quantitave tests on aforementioned audio files.
=>Changed training hyperparameters for slightly improved accuracies at the cost of a slightly longer training time (it is still incredibly fast on any mid to high tier gpu)
=>Other minor bug fixes.

The order of running and compiling the notebooks is as follows:
models.ipynb
utils.ipynb
prep_data.ipynb
train.ipynb
test.ipynb

Paths need to be added for specific sections to load/save audio files/weights/data in prep_data, train and test

The code requires the following dependancies:

```
keras==2.3.1
tensorflow==1.15.2
librosa==0.7.2
numpy==1.18.1
scipy==1.4.1
matplotlib==3.1.3
h5py==2.10.0
import_ipynb==0.1.3 #this is only for the connectivity of the jupyter notebooks and importing their modules should you wish to use scripting, this is optional
```
