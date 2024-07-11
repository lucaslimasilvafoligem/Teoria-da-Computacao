from automata.tm.mntm import MNTM

mntm3 = MNTM(
    states={'start', 'transition', 'done'},
    input_symbols={'a', 'b', '+'},
    tape_symbols={'a', 'b', '+', '.', 'X'},
    n_tapes=2,
    transitions={
        'start': {
          ('.', '.'): [('done', (('.', 'N'), ('.', 'N')))],
          ('a', '.'): [('transition', (('X', 'R'), ('a', 'R')))],
          ('b', '.'): [('transition', (('X', 'R'), ('b', 'R')))],
          ('+', '.'): [('transition', (('X', 'R'), ('.', 'N')))]
        },
        'transition': {
          ('.', '.'): [('done', (('.', 'N'), ('.', 'N')))],
          ('a', '.'): [('transition', (('X', 'R'), ('a', 'R')))],
          ('b', '.'): [('transition', (('X', 'R'), ('b', 'R')))],
          ('+', '.'): [('transition', (('X', 'R'), ('.', 'N')))]
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)
