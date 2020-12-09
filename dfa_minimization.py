class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_function.keys():
            self.current_state = None
        self.current_state = self.transition_function[(
            self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()

    def minimize(self):
        previous_k_eq = []
        next_k_eq = [self.accept_states,
                     self.states.difference(self.accept_states)]
        # print(next_k_eq)
        while previous_k_eq != next_k_eq:
            previous_k_eq = next_k_eq
            next_k_eq = []
            for group in previous_k_eq:
                new_groups = {}
                for state in group:
                    new_group = []
                    for alpha in self.alphabet:
                        new_alpha = self.transition_function[(state, alpha)]
                        new_group += [i for i in range(len(previous_k_eq))
                                      if new_alpha in previous_k_eq[i]]
                    if tuple(new_group) in new_groups:
                        new_groups[tuple(new_group)].add(state)
                    else:
                        new_groups[tuple(new_group)] = set(state)
                next_k_eq += [i for i in new_groups.values()]

        new_transition_function = dict()
        self.states = set(''.join(state) for state in next_k_eq)
        # Changes Starting States
        for state in self.states:
            if self.start_state in state:
                self.start_state = state

        # Changing Transistion States
        for ((key_string, key_trans), value) in self.transition_function.items():
            for state in self.states:
                if key_string in state:
                    new_transition_function[(state, key_trans)] = value
        for ((key_string, key_trans), value) in new_transition_function.items():
            for state in self.states:
                if value in state:
                    new_transition_function[(key_string, key_trans)] = state

        # Changing New Accept States
        newAcceptState = set()
        for state in self.states:
            for accept in self.accept_states:
                if accept in state:
                    newAcceptState.add(state)

        self.accept_states = newAcceptState
        self.transition_function = new_transition_function
