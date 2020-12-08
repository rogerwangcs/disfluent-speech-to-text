#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from os.path import join
from random import shuffle

TEST_PCT = 0.2

# folder where audio is
# AUDIO_FOLDER = 'augmented-data-big'
AUDIO_FOLDER = '/home/ubuntu/nlp/augmented-data-big'

speakers = [x for x in os.listdir(AUDIO_FOLDER) if '.' not in x]
shuffle(speakers)

test_num = int(TEST_PCT * len(speakers))

train_speakers = speakers[test_num:]
test_speakers = speakers[:test_num]

print(len(train_speakers), 'train')
print(len(test_speakers), 'test')
print(len(speakers), 'total')

assert len(train_speakers) + len(test_speakers) == len(speakers)

with open('train_speakers.txt', 'w') as aus:
	for s in train_speakers:
		aus.write(s + '\n')

with open('test_speakers.txt', 'w') as aus:
	for s in test_speakers:
		aus.write(s + '\n')


