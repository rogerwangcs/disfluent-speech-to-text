#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re
from os.path import join

OUTPUT_FOLDER = 'data/train/'

wavscp = open(OUTPUT_FOLDER+'wav.scp', 'w')
utt2spk = open(OUTPUT_FOLDER+'utt2spk', 'w')
text = open(OUTPUT_FOLDER+'text', 'w')

FOLDER = 'augmented-data-big'

i = 0

# for each speaker
for speaker in sorted([x for x in os.listdir(FOLDER) if not x.startswith('.')]):
	
	wavfiles = sorted([x for x in os.listdir(join(FOLDER, speaker)) if x.endswith('.wav')])
	
	# for each .wav file
	for wavfile in wavfiles:
		
		utt = wavfile[:-4] # utterance id
	
		# write file info to wav.scp
		wavscp.write(utt + ' ' + join(os.getcwd(), FOLDER, speaker, wavfile) + '\n')
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
