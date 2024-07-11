from automata.tm.dtm import DTM

dtm2 = DTM(
    states={'start', 'done'},
    input_symbols={'a', 'b','+'},
    tape_symbols={'a', 'b', '+', '.'},
    transitions={
        'start' : {
            
        }
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)
    
