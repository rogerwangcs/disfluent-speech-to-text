#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from os.path import join

# output folders
TRAIN_FOLDER = sys.argv[1]
TEST_FOLDER = sys.argv[2]

# folder where audio is
# AUDIO_FOLDER = 'augmented-data-big'
AUDIO_FOLDER = '/home/ubuntu/nlp/augmented-data-big'

# list of speakers for training data
with open('train_speakers.txt', 'r') as ein:
	TRAIN_SPEAKERS = ein.read().strip().split('\n')

# list of speakers for testing data
with open('test_speakers.txt', 'r') as ein:
	TEST_SPEAKERS = ein.read().strip().split('\n')


# create files for TRAIN_FOLDER or TEST_FOLDER
def createFiles(OUTPUT_FOLDER, SPEAKERS):
	wavscp = open(OUTPUT_FOLDER+'wav.scp', 'w')
	utt2spk = open(OUTPUT_FOLDER+'utt2spk', 'w')
	text = open(OUTPUT_FOLDER+'text', 'w')
	corpus = open(OUTPUT_FOLDER+'corpus.txt', 'w')
	
	i = 0
	j = 0
	
	for speaker in sorted(SPEAKERS):
	# for speaker in sorted([x for x in os.listdir(AUDIO_FOLDER) if '.' not in x]):
		
		wavfiles = sorted([x for x in os.listdir(join(AUDIO_FOLDER, speaker)) if x.endswith('.wav')])
		
		for wavfile in wavfiles:
		
			utt = wavfile[:-4] # utterance id
	
			# write file info to wav.scp
			wavscp.write(utt + ' ' + join(os.getcwd(), AUDIO_FOLDER, speaker, wavfile) + '\n')
			# write speaker info to utt2spk
			utt2spk.write(utt + ' ' + speaker + '\n')
			# write transcription to text
			with open(join(AUDIO_FOLDER, speaker, utt+'.lab')) as ein:
				utt_text = ein.read().strip()
				text.write(utt + ' ' + utt_text + '\n')
				# write transcription to corpus.txt
				corpus.write(utt_text + '\n')
			
			i += 1
	
		j += 1
		print(speaker)

	print(OUTPUT_FOLDER)
	print('num speakers', j)
	print('num utterances', i, '\n')
	wavscp.close()
	utt2spk.close()
	text.close()
	return
	
createFiles(TRAIN_FOLDER, TRAIN_SPEAKERS)
createFiles(TEST_FOLDER, TEST_SPEAKERS)


