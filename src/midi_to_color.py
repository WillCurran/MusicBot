# colors for context highlighting in printouts
colors = {
    'A' : '\u001b[38;5;76m',
    'A#' :  '\u001b[38;5;174m',
	'B' :  '\u001b[38;5;44m',
    'C' :  '\u001b[38;5;160m',
    'C#' :  '\u001b[38;5;135m',
    'D' :  '\u001b[38;5;226m',
    'D#' :  '\u001b[38;5;204m',
    'E' :  '\u001b[38;5;159m',
    'F' :  '\u001b[38;5;124m',
    'F#' :  '\u001b[38;5;11m',
    'G' :  '\u001b[38;5;208m',
    'G#' :  '\u001b[38;5;219m',
    'ENDC' :  '\033[0m',
    'note_on' : '\u001b[38;5;177m',
    'instr' : '\u001b[38;5;177m',
    '0x' : '\u001b[38;5;27m',
    'None' : '\u001b[38;5;27m',
    'const' : '\u001b[38;5;33m',
    'arg' : '\u001b[38;5;254m',
    'numeric' : '\u001b[38;5;84m',
    'string' : '\u001b[38;5;172m'
}
# root notes
roots = {
    21 : 'A',
    22: 'A#',
    23: 'B',
    24: 'C',
    25: 'C#',
    26: 'D',
    27: 'D#',
    28: 'E',
    29: 'F',
    30: 'F#',
    31: 'G',
    32: 'G#'
}

# note from midi
def getNote(m):
    if m < 21:
        return 'A'
    if m in roots.keys():
        return roots[m]
    return getNote(m-12)

def midiToColor(m):
    return colors[getNote(m)]
