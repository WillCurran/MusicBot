# USES THROUGH_PORT 0
# prints instructions as they are carried out for aesthetics
# requires substantive code to be identical in both functions

import mido
import time
import dis
import random
from more_itertools import peekable

# Amount to wait before sending off note sequence
MAX_NOTE_DELAY = 2.0
MAX_SEQ_LEN = 32

PRINT_DIR = './print_outs/'
counter = 0

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
                    # add note to sequence
                    if msg.type == 'note_on':
                        note_seq.append(msg.note)
            # sequence is complete. save and revert to waiting
            else:
                print(note_seq, flush=True)
                note_seq = []

    # NOTES:
    # - try adding note_off events and/or no event spacers?

def print_line_bytes(instructions, line):
    global counter
    s = str(instructions[line])
    f = open(PRINT_DIR + str(counter), 'w')
    f.write(s)
    f.close()
    counter += 1
    

def instructions_to_list(instructions):
    l = []
    instr = next(instructions, None)
    while instr != None:
        if instr.starts_line != None:
            l.append("")
        s = "instr %s<%s> arg=%s argval=%s offset=%s\n" % (str(hex(instr.opcode)), str(instr.opname), str(instr.arg), str(instr.argval), str(instr.offset))
        l[-1] += s
        instr = next(instructions, None)
    return l

def read_midi_printcode():
    instructions = instructions_to_list(dis.get_instructions(read_midi, first_line=-1))
    with mido.open_input('Midi Through:Midi Through Port-0 14:0') as inport:
        print_line_bytes(instructions, 0)
        note_seq = []
        print_line_bytes(instructions, 1)
        last_note_played = -1
        print_line_bytes(instructions, 2)
        print_line_bytes(instructions, 3)
        while True:
            if waiting_for_note(note_seq, last_note_played):
                for msg in inport.iter_pending():
                    print_line_bytes(instructions, 5)
                    last_note_played = time.time()
                    print_line_bytes(instructions, 6)
                    # add note to sequence
                    if msg.type == 'note_on':
                        print_line_bytes(instructions, 7)
                        note_seq.append(msg.note)
                        print_line_bytes(instructions, 8)
    # sequence is complete. save and revert to waiting
            else:
                print_line_bytes(instructions, 9)
                print(note_seq, flush=True)
                note_seq = []

    # NOTES:
    # - try adding note_off events and/or no event spacers?
    

if __name__ == "__main__":
    counter = 0
    read_midi_printcode()