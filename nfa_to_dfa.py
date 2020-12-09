from dfa_minimization import DFA
from nfa_simulator import NFA


class NFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.alphabet.add("lam")
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


class DFAfromNFA:
    """class for building dfa from e-nfa and minimise it"""

    def __init__(self, nfa):
        print("Starting")
        # self.buildDFA(nfa)
        # self.minimise()

        # d = DFA(states, alphabet, tf, start_state, accept_states)

    def lambda_getter(self, nfa, state):
        if (state, "lam") not in nfa.transition_function:
            return [state]
        else:
            return [state] + self.lambda_getter(nfa, "".join(nfa.transition_function[(state, "lam")]))

    def buildDFA(self, nfa):
        dfa_tf = {}
        dfa_alphabet = nfa.alphabet
        dfa_alphabet.remove("lam")
        dfa_states = set()
        dfa_start_state = nfa.start_state
        dfa_accept_states = set()
        # Adding all states
        dfa_states.add("".join(self.lambda_getter(nfa, nfa.start_state)))
        nfa_states = nfa.states
        for state in nfa.states:
            for alpha in nfa.alphabet:
                if (state, alpha) in nfa.transition_function:
                    current_state = "".join(
                        nfa.transition_function[(state, alpha)])
                    current_state = "".join(
                        self.lambda_getter(nfa, current_state))
                    if current_state not in dfa_states:
                        dfa_states.add(current_state)

        current_states = dfa_states.copy()

        dfa_tf["trash", 0] = "trash"
        dfa_tf[("trash", 1)] = "trash"
        # Get accept states

        while len(current_states) != 0:
            current_state = current_states.pop()
            for alpha in nfa.alphabet:
                current_transition = set()
                for nfa_state in list(current_state):
                    if (nfa_state, alpha) in nfa.transition_function:
                        current_transition.add(
                            "".join(nfa.transition_function[(nfa_state, alpha)]))
                transition = "".join(current_transition)
                transition = "".join(list(set(list(transition))))
                if transition != "":
                    dfa_tf[(current_state, alpha)] = transition
                    if transition not in dfa_states:
                        dfa_states.add(transition)
                        current_states.add(transition)
                else:
                    dfa_tf[(current_state, alpha)] = "trash"

        print(nfa.accept_states)
        for state in dfa_states:
            for accept_state in nfa.accept_states:
                if accept_state in state:
                    dfa_accept_states.add(state)
        print("DFA States:  ")
        print(dfa_states)
        print()
        print("DFA Alphabet:  ")
        print(dfa_alphabet)
        print()
        print("DFA Transition Function:  ")
        print(dfa_tf)
        print()
        print("DFA Start State:  ")
        print(dfa_start_state)
        print()
        print("DFA Accept States:  ")
        print(dfa_accept_states)
        print()
        return DFA(dfa_states, dfa_alphabet, dfa_tf, dfa_start_state, dfa_accept_states)


states = {'a', 'b', 'c'}
alphabet = {0, 1}
tf = dict()

tf[("a", 0)] = ["b", "c"]
tf[("a", "lam")] = ["b"]
tf[("a", 1)] = ["a"]
tf[("b", 1)] = ["b", "c"]
tf[("c", 0)] = ["c"]
tf[("c", 1)] = ["c"]


start_state = 'a'
accept_states = {'c'}

d = NFA(states, alphabet, tf, start_state, accept_states)

dfa_convert = DFAfromNFA(d)

dfa = dfa_convert.buildDFA(d)

# print(d.run_with_input_list([1, 0, 1, 1, 0, 0, 0]))
# print("Accept States:  ", d.accept_states)
# print("States:  ", d.states)
# print('Transition Function:  ', d.transition_function)
