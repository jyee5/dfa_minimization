from dfa_minimization import DFA
from nfa_simulator import NFA


def dfa_min_test():

    # Minimize Test 1
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
    test_cases_accept = [[0, 0], [0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1]]
    test_case_reject = [[0, 0, 1, 0], [1, 0, 1], [1, 1, 1], [0, 1, 1], []]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    d.minimize()
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"

    # Minimize Test 2
    states = {'s', 'a', 'b', 'e', 'd'}
    alphabet = {0, 1}
    tf = dict()
    tf[("s", 0)] = "a"
    tf[("s", 1)] = "d"
    tf[("d", 0)] = "d"
    tf[("d", 1)] = "d"
    tf[("e", 0)] = "d"
    tf[("e", 1)] = "d"
    tf[("b", 0)] = "s"
    tf[("b", 1)] = "e"
    tf[("a", 0)] = "b"
    tf[("a", 1)] = "e"
    start_state = 's'
    accept_states = {'s'}
    d = DFA(states, alphabet, tf, start_state, accept_states)
    test_cases_accept = [[0, 0, 0], [], [
        0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    test_case_reject = [[0, 0, 1, 0], [1, 0, 1], [1, 1, 1], [0, 1, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    d.minimize()
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"


def nfa_sim_test():
    # Test 1 L = {w | w begins with 010 followed by anything and ends with another 010} alpha = {0, 1}
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    alphabet = {0, 1}
    tf = dict()

    tf[("a", 0)] = ["b"]
    tf[("b", 1)] = ["c"]
    tf[("c", 0)] = ["d"]
    tf[("d", 0)] = ["d", "e"]
    tf[("d", 1)] = ["d"]
    tf[("e", 1)] = ["f"]
    tf[("f", 0)] = ["g"]

    start_state = 'a'
    accept_states = {'g'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    test_cases_accept = [[0, 1, 0, 0, 1, 0], [
        0, 1, 0, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0]]
    test_case_reject = [[0, 0, 1, 0], [1, 0, 1], [1, 1, 1],
                        [0, 1, 1], [], [0, 1, 0, 0, 1, 0, 0, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"

    # Test 2 L = {w | w contains an even number of 0's OR even number of 1's} alpha = {0, 1}
    states = {'a', 'b', 'c', 'd', 'e'}
    alphabet = {0, 1}
    tf = dict()

    tf[("a", "lam")] = ["b", "d"]
    tf[("b", 1)] = ["b"]
    tf[("b", 0)] = ["c"]
    tf[("c", 1)] = ["c"]
    tf[("c", 0)] = ["b"]
    tf[("d", 1)] = ["e"]
    tf[("d", 0)] = ["d"]
    tf[("e", 1)] = ["d"]
    tf[("e", 0)] = ["e"]

    start_state = 'a'
    accept_states = {'b', 'd'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    test_cases_accept = [[0, 1, 0, 0, 1, 0], [
        1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0], [], [1, 1, 1], [0, 0, 0]]
    test_case_reject = [[0, 0, 1, 0], [
        1, 0, 1, 1], [1, 0], [0, 1, 0, 0, 1, 0, 0, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        print(test)
        assert d.run_with_input_list(test) == True, "Should be True"


if __name__ == "__main__":
    dfa_min_test()
    nfa_sim_test()
    print("Everything passed")
