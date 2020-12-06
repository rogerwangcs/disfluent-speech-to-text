#!/Users/christine/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, re
from os.path import join

OUTPUT_FOLDER = 'data/train/'

wavscp = open(OUTPUT_FOLDER+'wav.scp', 'w')
utt2spk = open(OUTPUT_FOLDER+'utt2spk', 'w')
text = open(OUTPUT_FOLDER+'text', 'w')
corpus = open(OUTPUT_FOLDER+'corpus.txt', 'w')

FOLDER = 'augmented-data-big'

i = 0

# for each speaker
for speaker in sorted([x for x in os.listdir(FOLDER) if '.' not in x]):
	
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
                    utt_text = ein.read().strip()
		    text.write(utt + ' ' + utt_text + '\n')
                    # write transcription to corpus.txt
                    corpus.write(utt_text + '\n')
		    
		# print(wavfile)
		i += 1
	
	print(speaker)

print('total', i)

wavscp.close()
utt2spk.close()
text.close()
