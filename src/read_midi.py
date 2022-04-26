# USES THROUGH_PORT 0
import mido
import time

# Amount to wait before sending off note sequence
MAX_NOTE_DELAY = 2.0
MAX_SEQ_LEN = 32

def waiting_for_note(seq, t):
    # waiting for 1st note or a subsequent note from user
    return (seq == []) or ((len(seq) < MAX_SEQ_LEN) and (time.time() - t < MAX_NOTE_DELAY))

def read_midi():
    with mido.open_input('Midi Through:Midi Through Port-0 14:0') as inport:
        note_seq = []
        last_note_played = -1
        while True:
            if waiting_for_note(note_seq, last_note_played):
                for msg in inport.iter_pending():
                    last_note_played = time.time()
                    # TODO - play the note (send to output device that will be played by a synth program)

                    # add note to sequence
                    if msg.type == 'note_on':
                        note_seq.append(msg.note)
    # sequence is complete. save and revert to waiting
            else:
                print(note_seq, flush=True)
                note_seq = []

    # NOTES:
    # - try adding note_off events and/or no event spacers?

if __name__ == "__main__":
    read_midi()