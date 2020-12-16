# pete alonzi (lpa2a@virginia.edu)
# a smell test for the adventure zone dataset
# 2020-12-14
# https://github.com/alonzi/Bayesian-Adventure-Zone
# coding practice

#
##
### NB: this is quick and dirty, don't use this form, if you don't liek it, pull request it
##
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read in and munge
rolls = pd.read_csv('../TravisRollsDataset.csv')          # read in to data frame
print(f'There are {len(rolls)} rolls in this dataset.')   # print out size of initial dataset
rolls = rolls[rolls['adv'].isna()]                        # drop advantage/disadvantage
rolls['d20'] = rolls['roll']-rolls['mod']                 # compute d20 roll
print(f'There are {len(rolls)} rolls in this munged dataset.')   # print out size of remaining dataset



# diagnostic plots
rolls['d20'].plot.hist(bins=26,range=(-5,20),title='Travis d20 rolls')

# expected distribution
sim_rolls = pd.DataFrame(np.random.randint(1,21,151))
sim_rolls.plot.hist(bins=26,range=(-5,20),color='red',title='numpy d20 rolls')


# show plots
plt.show()


# findings
# 1. six rolls are smaller than their modifier - oopsie
# 2. Doesn't look like you can say there is cheating on those d20 rolls


'''
## things i googled
# pandas syntax read_csv
# pandas show top ten rows of dataframe
# install pandas
# install anaconda
# when did anaconda get terrible
# install miniconda
# bash set environment variable
# add directory to path
# install pandas
# when did windows get so terrible
# install pandas vs code
# vs code use conda environment
# get list of installed packages in conda environment
# change vs code to activate conda environment in bash
# get vs code run python to use bash
# matplotlib documentation hist
# pandas plot documentation hist
# vs code matplotlib figure does not appear
# matplotlib example in vs code
# pandas syntax create new column in dataframe
# matplotlib histogram bin definition
# matplotlib documentation hist
# numpy flan rand int
# matplotlib change histogram color
'''

'''
## conda environment setup
# conda create -n env-smell-test
# source /c/Users/petea_000/miniconda3/etc/profile.d/conda.sh # required to allow 'conda activate'
# conda activate env-smell-test
# conda install pandas
# conda install matplotlib
##

## terminal environment load - every session
# I am using VS code and it is different that before. When starting a new session issue the following
#  1. source /c/Users/petea_000/miniconda3/etc/profile.d/conda.sh # refactor - remove absolute path
#  2. conda activate env-smell-test
#  3. cd Desktop/Bayesian-Adventure-Zone/alonzi-wd/ # refactor - remove absolute path
# to run code right click in editor and select 'Run python file interminal'
# when i run the code with ctrl + F5 it tries to activate the environment in dos i don't know how to force it to bash
# nB: this is clearly a poor solution, see refactor flag for improvement
##
'''