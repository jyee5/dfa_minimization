class NFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet.add("lam")
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = [start_state]

    def transition_to_state_with_input(self, input_value):
        self.lambda_check()
        new_current = []
        # Gets the multiple changes for each state, and checking if one will be accepted
        for current in self.current_state:
            if (current, input_value) not in self.transition_function.keys():
                new_current += []
            else:
                for i in self.transition_function[(current, input_value)]:
                    new_current += [i]
        self.current_state = new_current

    def in_accept_state(self):
        # Checks all values in the final states to see if one will be accepted
        for i in self.current_state:
            if i in self.accept_states:
                return True
        return False

    def go_to_initial_state(self):
        self.current_state = [self.start_state]

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for input in input_list:
            self.transition_to_state_with_input(input)
        self.lambda_check()
        return self.in_accept_state()

    # Handles Lambda Moves
    def lambda_check(self):
        for current in self.current_state:
            if (current, "lam") in self.transition_function.keys():
                for i in self.transition_function[(current, "lam")]:
                    self.current_state += [i]
