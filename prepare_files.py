#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re, pandas as pd
from os.path import join


wavscp = open('wav.scp', 'w')
utt2spk = open('utt2spk', 'w')
text = open('text', 'w')

FOLDER = 'augmented-data-big'

i = 0

# for each speaker
for speaker in [x for x in os.listdir(FOLDER) if not x.startswith('.')]:
	
	wavfiles = [x for x in os.listdir(join(FOLDER, speaker)) if x.endswith('.wav')]
	
	# for each .wav file
	for wavfile in wavfiles:
		
		utt = wavfile[:-4] # utterance id
	
		# write file info to wav.scp
		wavscp.write(utt + ' ' + join(FOLDER, speaker, wavfile) + '\n')
		# write speaker info to utt2spk
		utt2spk.write(utt + ' ' + speaker + '\n')
		# write transcription to text
		with open(join(FOLDER, speaker, utt+'.lab')) as ein:
			text.write(utt + ' ' + ein.read() + '\n')
			
		# print(wavfile)
		i += 1
	
	print(speaker)

print('total', i)

wavscp.close()
utt2spk.close()
text.close()