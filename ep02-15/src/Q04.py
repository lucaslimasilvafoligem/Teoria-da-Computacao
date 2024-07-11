from automata.tm.mntm import MNTM

mntm4 = MNTM(
    states={'start', 'done'},
    input_symbols={'a', 'b', '#'},
    tape_symbols={'a', 'b', '#', '.'},
    n_tapes=2,
    transitions={
      'start': {
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'},
)

mntm4 = MNTM(
    states={'start', 'adds', 'addw', 'compare', 'compare-loop', 'fim-fita2', 'done'},
    input_symbols={'a', 'b', '#'},
    tape_symbols={'a', 'b', '#', '.'},
    n_tapes=2,
    transitions={
        'start': {
            ('a', '.'): [('adds', (('a', 'R'), ('a', 'R')))],
            ('b', '.'): [('adds', (('b', 'R'), ('b', 'R')))],
            ('#', '.'): [('addw', (('#', 'R'), ('#', 'N')))],
        },
        'adds': {
            ('a', '.'): [('adds', (('a', 'R'), ('a', 'R')))],
            ('b', '.'): [('adds', (('b', 'R'), ('b', 'R')))],
            ('#', '.'): [('addw', (('#', 'R'), ('#', 'N')))],
        },
        'addw': {
            ('a', '#'): [('addw', (('a', 'R'), ('#', 'N')))],
            ('b', '#'): [('addw', (('b', 'R'), ('#', 'N')))],
            ('.', '#'): [('compare', (('.', 'L'), ('#', 'L')))],
            ('.', '#'): [('compare', (('.', 'L'), ('#', 'L')))],  
        },
        'compare': {
            ('a', '.'): [('done', (('a', 'N'), ('.', 'N')))],
            ('b', '.'): [('done', (('b', 'N'), ('.', 'N')))],
            ('#', '.'): [('done', (('#', 'N'), ('.', 'N')))],
            ('a', 'a'): [('compare-loop', (('a', 'N'), ('a', 'N')))],
            ('b', 'b'): [('compare-loop', (('b', 'N'), ('b', 'N')))],
            ('b', 'a'): [('compare-loop', (('b', 'L'), ('a', 'N')))],
            ('a', 'b'): [('compare-loop', (('a', 'L'), ('b', 'N')))],
        }, 
        'compare-loop': {
            ('#', '.'): [('done', (('#', 'N'), ('.', 'N')))],
            ('a', '.'): [('done', (('a', 'N'), ('.', 'N')))],
            ('b', '.'): [('done', (('b', 'N'), ('.', 'N')))],
            ('a', 'a'): [('compare-loop', (('a', 'L'), ('a', 'L')))],
            ('b', 'b'): [('compare-loop', (('b', 'L'), ('b', 'L')))],
            ('a', 'b'): [('fim-fita2', (('a', 'N'), ('b', 'N')))],
            ('b', 'a'): [('fim-fita2', (('b', 'N'), ('a', 'N')))],
        },
          'fim-fita2': {
            ('a', 'b'): [('fim-fita2', (('a', 'N'), ('b', 'R')))],
            ('b', 'a'): [('fim-fita2', (('b', 'N'), ('a', 'R')))],              
            ('a', 'a'): [('fim-fita2', (('a', 'N'), ('a', 'R')))],
            ('b', 'b'): [('fim-fita2', (('b', 'N'), ('b', 'R')))],
            ('a', '#'): [('compare', (('a', 'N'), ('#', 'L')))],
            ('b', '#'): [('compare', (('b', 'N'), ('#', 'L')))],
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)
