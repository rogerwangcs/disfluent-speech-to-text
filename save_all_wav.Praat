
save_directory$ = "/Users/rogerwangcs/Desktop"

clearinfo
pause select all sounds to be used for this operation
numberOfSelectedSounds = numberOfSelected ("Sound")

for thisSelectedSound to numberOfSelectedSounds
	sound'thisSelectedSound' = selected("Sound",thisSelectedSound)
endfor

for thisSound from 1 to numberOfSelectedSounds
    select sound'thisSound'
	name$ = selected$("Sound")

    Save as WAV file... 'save_directory$'/'name$'.wav

endfor

#re-select the sounds
select sound1
for thisSound from 2 to numberOfSelectedSounds
    plus sound'thisSound'
endfor