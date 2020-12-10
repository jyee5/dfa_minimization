from dfa_minimization import DFA
from nfa_simulator import NFA


class DFAfromNFA:
    """class for building dfa from e-nfa and minimise it"""

    def __init__(self, nfa):
        self.nfa = nfa
        # self.buildDFA(nfa)
        # self.minimise()

        # d = DFA(states, alphabet, tf, start_state, accept_states)

    def lambda_getter(self, nfa, state):
        results = set()
        for i in state:
            # print(i)
            results.add(i)
            if (i, "lam") in nfa.transition_function:
                for x in self.lambda_getter(nfa,
                                            set(nfa.transition_function[(i, "lam")])):
                    results.add(x)
        return set(results)

    def buildDFA(self, nfa):
        dfa_tf = {}
        dfa_alphabet = nfa.alphabet
        dfa_alphabet.remove("lam")
        dfa_states = set()
        dfa_start_state = "".join(list(self.lambda_getter(
            nfa, set(list(nfa.start_state)))))
        dfa_accept_states = set()
        # Adding all states
        dfa_states.add("".join(list(self.lambda_getter(
            nfa, set(list(nfa.start_state))))))  # Adds first state
        dfa_states.add("trash")
        # Adds following states
        nfa_states = nfa.states
        for state in nfa.states:
            for alpha in nfa.alphabet:
                if (state, alpha) in nfa.transition_function:
                    current_state = "".join(
                        nfa.transition_function[(state, alpha)])
                    current_state = "".join(
                        list(self.lambda_getter(nfa, current_state)))
                    if current_state not in dfa_states:
                        dfa_states.add(current_state)

        current_states = dfa_states.copy()

        dfa_tf["trash", 0] = "trash"
        dfa_tf[("trash", 1)] = "trash"

        # Get Transition Function
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

        # Get accept states
        for state in dfa_states:
            for accept_state in nfa.accept_states:
                if accept_state in state:
                    dfa_accept_states.add(state)
        # print("DFA States:  ")
        # print(dfa_states)
        # print()
        # print("DFA Alphabet:  ")
        # print(dfa_alphabet)
        # print()
        # print("DFA Transition Function:  ")
        # print(dfa_tf)
        # print()
        # print("DFA Start State:  ")
        # print(dfa_start_state)
        # print()
        # print("DFA Accept States:  ")
        # print(dfa_accept_states)
        # print()
        return DFA(dfa_states, dfa_alphabet, dfa_tf, dfa_start_state, dfa_accept_states)


# states = {'a', 'b', 'c'}
# alphabet = {0, 1}
# tf = dict()

# tf[("a", 0)] = ["b", "c"]
# tf[("a", "lam")] = ["b"]
# tf[("a", 1)] = ["a"]
# tf[("b", 1)] = ["b", "c"]
# tf[("c", 0)] = ["c"]
# tf[("c", 1)] = ["c"]


# start_state = 'a'
# accept_states = {'c'}

# d = NFA(states, alphabet, tf, start_state, accept_states)

# dfa_convert = DFAfromNFA(d)

# dfa = dfa_convert.buildDFA(d)

# print(d.run_with_input_list([1, 0, 1, 1, 0, 0, 0]))
# print("Accept States:  ", d.accept_states)
# print("States:  ", d.states)
# print('Transition Function:  ', d.transition_function)
