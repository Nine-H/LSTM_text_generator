#! /usr/bin/env python3

import numpy as np
import pandas as pd

text=open("input.txt",'r')

vocab_size=10000
data, count, dictionary, reverse_dictionary=collect_data(vocabulary_size=vocab_size)

window_size=3
vector_dim=300
epochs=100000

valid_size=16
valid_window=100
valid_examples=np.random.choice(valid_window, valid_size, replace=False)
