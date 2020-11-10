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
        return self.current_state in accept_states

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
                    for alpha in alphabet:
                        new_alpha = self.transition_function[(state, alpha)]
                        new_group += [i for i in range(len(previous_k_eq))
                                      if new_alpha in previous_k_eq[i]]
                    if tuple(new_group) in new_groups:
                        new_groups[tuple(new_group)].add(state)
                    else:
                        new_groups[tuple(new_group)] = set(state)
                next_k_eq += [i for i in new_groups.values()]

        self.states = set(''.join(state) for state in next_k_eq)
        print(self.states)
        newTrasitionFunc = dict()
        newAcceptState = set()
        for state in self.states:
            if state in self.accept_states:
                newAcceptState.add(state)
            newTrasitionFunc[(state, 0)] = self.transition_function[(state, 0)]
            newTrasitionFunc[(state, 1)] = self.transition_function[(state, 1)]
        self.accept_states = newAcceptState
        self.transition_function = newTrasitionFunc
        # print(newTrasitionFunc)


states = {'a', 'e', 'g', 'k', 'n', 'm'}
alphabet = {0, 1}
tf = dict()
tf[("a", 0)] = "e"
tf[("a", 1)] = "m"
tf[("e", 0)] = "g"
tf[("e", 1)] = "n"
tf[("g", 0)] = "k"
tf[("g", 1)] = "g"
tf[("k", 0)] = "m"
tf[("k", 1)] = "n"
tf[("m", 0)] = "m"
tf[("m", 1)] = "k"
tf[("n", 0)] = "k"
tf[("n", 1)] = "m"

start_state = 'a'
accept_states = {'e', 'g'}

d = DFA(states, alphabet, tf, start_state, accept_states)

print(d.run_with_input_list([0, 1]))
print(d.run_with_input_list([1, 0]))
d.minimize()
print(d.accept_states)
print(d.states)
# print(d.run_with_input_list([0, 1]))
# print(d.start_state)
# print(d.run_with_input_list([1, 0]))
