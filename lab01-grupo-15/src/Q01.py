from automata.fa.dfa import DFA


dfa01 = DFA(
        states={'q0', 'q1', 'q2', 'q3'}, 
        input_symbols={'a', 'b'}, 
        transitions={
            'q0': {'a': 'q1', 'b': 'q3'},
            'q1': {'a': 'q3', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q3'},
            'q3': {'a': 'q3', 'b': 'q3'}
        }, 
        initial_state='q0', 
        final_states={'q2'}
)


    
