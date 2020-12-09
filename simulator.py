from dfa_minimization import DFA
from nfa_simulator import NFA


def nfa_sim():
    states = {'a', 'b', 'c', 'd', 'e'}
    alphabet = {0, 1}
    tf = dict()

    tf[("a", "lam")] = ["b"]
    tf[("b", 1)] = ["c"]
    tf[("c", 0)] = ["d"]
    tf[("d", 1)] = ["d", "e"]
    tf[("d", 0)] = ["d"]
    tf[("e", 0)] = ["e"]
    tf[("e", 1)] = ["e"]

    start_state = 'a'
    accept_states = {'e'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    print(d.run_with_input_list([1, 0, 1, 1, 0, 0, 0]))
    print("Accept States:  ", d.accept_states)
    print("States:  ", d.states)
    print('Transition Function:  ', d.transition_function)


def dfa_min_sim():
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

    print(d.run_with_input_list([0, 0, 1, 0]))
    print(d.run_with_input_list([1, 0]))
    d.minimize()
    print("Accept States:  ", d.accept_states)
    print("States:  ", d.states)
    print('Transition Function:  ', d.transition_function)
    print(d.run_with_input_list([0, 0, 1, 0]))
    print(d.run_with_input_list([1, 0]))


nfa_sim()
