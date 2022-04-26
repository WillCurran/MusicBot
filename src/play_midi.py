# USES THROUGH_PORT 1

import mido
import time
import sys
import midi_to_color

# delay multiplier
NOTE_DELAY = 2.0
FINAL_DELAY = 1.0

print(mido.get_output_names())

with mido.open_output('Midi Through:Midi Through Port-1 14:1') as outport:
	print("opening midi file:", sys.argv[1])
	mid = mido.MidiFile(sys.argv[1])
	for msg in mid.play():
		if hasattr(msg, 'note'):
			notecol = midi_to_color.colors['note_on']
			endc = midi_to_color.colors['ENDC']
			argcol = midi_to_color.colors['arg']
			numcol = midi_to_color.colors['numeric']
			s = f"{notecol}note_on{endc} {argcol}channel{endc}={numcol}0{endc} {argcol}note{endc}={midi_to_color.midiToColor(msg.note)}{msg.note}{endc} {argcol}velocity{endc}={numcol}{msg.velocity} {argcol}time{endc}={numcol}{msg.time}{endc}"
			print(s)
		else:
			print(msg)
		outport.send(msg)
		delay_start = time.time()
		while(time.time() - delay_start < NOTE_DELAY * msg.time):
			pass
delay_start = time.time()
while(time.time() - delay_start < FINAL_DELAY):
	pass
print("Done playing midi file.")
