#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re, pandas as pd
from os.path import join


wavscp = open('wav.scp', 'w')
utt2spk = open('utt2spk', 'w')
text = open('text', 'w')

# for each speaker
for speaker in ['19', '26', '27']:
	
	wavfiles = [x for x in os.listdir(join('augmented-data', speaker)) if x.endswith('.wav')]
	
	# for each .wav file
	for wavfile in wavfiles:
		
		utt = wavfile[:-4] # utterance id
	
		# write file info to wav.scp
		wavscp.write(utt + ' ' + join('augmented-data', speaker, wavfile) + '\n')
		# write speaker info to utt2spk
		utt2spk.write(utt + ' ' + speaker + '\n')
		# write transcription to text
		with open(join('augmented-data', speaker, utt+'.lab')) as ein:
			text.write(utt + ' ' + ein.read() + '\n')
			
		print(wavfile)


wavscp.close()
utt2spk.close()
text.close()