from dfa_minimization import DFA
from nfa_simulator import NFA
from nfa_to_dfa import DFAfromNFA
import string


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
    assert len(d.states) == 4, "Should have 4 states"

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
    assert len(d.states) == 4, "Should have 4 states"

    # Minimize Test 3
    states = {'s', 'b', 'a', 'c', 'd'}
    alphabet = {0, 1}
    tf = dict()
    tf[("s", 0)] = "a"
    tf[("s", 1)] = "b"
    tf[("b", 0)] = "a"
    tf[("b", 1)] = "c"
    tf[("a", 0)] = "c"
    tf[("a", 1)] = "d"
    tf[("d", 0)] = "c"
    tf[("d", 1)] = "c"
    tf[("c", 0)] = "c"
    tf[("c", 1)] = "c"
    start_state = 's'
    accept_states = {'d', 'c'}
    d = DFA(states, alphabet, tf, start_state, accept_states)
    test_cases_accept = [[1, 0, 1], [0, 1],
                         [0, 0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0]]
    test_case_reject = [[], [1], [0]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    d.minimize()
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    assert len(d.states) == 4, "Should have 4 states"

    # Minimize Test 4
    # HUGE MINIMIZATION
    states = {'s', 'b', 'a', 'c', 'd', 'e', 'f', 'g', 'm', 'n', 'p'}
    alphabet = {0, 1}
    tf = dict()
    tf[("s", 0)] = "a"
    tf[("s", 1)] = "p"
    tf[("b", 0)] = "c"
    tf[("b", 1)] = "m"
    tf[("a", 0)] = "b"
    tf[("a", 1)] = "n"
    tf[("d", 0)] = "e"
    tf[("d", 1)] = "f"
    tf[("c", 0)] = "m"
    tf[("c", 1)] = "d"
    tf[("m", 0)] = "n"
    tf[("m", 1)] = "p"
    tf[("p", 0)] = "n"
    tf[("p", 1)] = "n"
    tf[("n", 0)] = "m"
    tf[("n", 1)] = "m"
    tf[("e", 0)] = "g"
    tf[("e", 1)] = "f"
    tf[("f", 0)] = "e"
    tf[("f", 1)] = "g"
    tf[("g", 0)] = "f"
    tf[("g", 1)] = "f"
    start_state = 's'
    accept_states = {'d', 'e', 'f', 'g'}
    d = DFA(states, alphabet, tf, start_state, accept_states)
    test_cases_accept = [[0, 0, 0, 1, 0, 1, 1], [
        0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]]
    test_case_reject = [[], [1], [0], [
        0, 1, 0, 0, 1, 1, 1], [1, 0, 1], [1, 1, 1, 1, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    d.minimize()
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    assert len(d.states) == 6, "Should have 6 states"

    # Minimize Test 5
    # Includes lambda being accepted
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    alphabet = {0, 1}
    tf = dict()
    tf[("a", 0)] = "b"
    tf[("a", 1)] = "c"
    tf[("b", 0)] = "d"
    tf[("b", 1)] = "e"
    tf[("c", 0)] = "e"
    tf[("c", 1)] = "d"
    tf[("d", 0)] = "f"
    tf[("d", 1)] = "g"
    tf[("e", 0)] = "g"
    tf[("e", 1)] = "f"
    tf[("f", 0)] = "b"
    tf[("f", 1)] = "c"
    tf[("g", 0)] = "c"
    tf[("g", 1)] = "b"
    start_state = "a"
    accept_states = {'a', 'g', 'f'}
    d = DFA(states, alphabet, tf, start_state, accept_states)
    test_cases_accept = [[], [0, 0, 0], [
        0, 0, 0, 1, 0, 0], [1, 1, 1]]
    test_case_reject = [[1], [0], [
        0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    d.minimize()
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"
    assert len(d.states) == 3, "Should have 6 states"


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
        assert d.run_with_input_list(test) == True, "Should be True"

    # Test 3 L1 = {w | w starts with 0 and ends with 0} alpha = {0, 1} L2 = 0... L = L1.L2
    # Beginning with Lambda and Accept state
    states = {'a', 'b', 'c', 'd', 'e'}
    alphabet = {0, 1}
    tf = dict()

    tf[("a", "lam")] = ["b"]
    tf[("b", 0)] = ["c"]
    tf[("c", 1)] = ["c"]
    tf[("c", 0)] = ["b", "d"]
    tf[("d", "lam")] = ["e"]
    tf[("f", "lam")] = ["a"]

    start_state = 'a'
    accept_states = {'f', 'a'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    test_cases_accept = [[]]
    test_case_reject = [[0], [0, 1, 1], [0, 0, 1, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"

    # Test 4 L1 = {w | w starts with 0 and ends with 0} alpha = {0, 1} L2 = {w | w is a binary string divisible by 8 and lambda is accepted}... L = L1.L2
    # Multiple Lambda States
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'z'}
    alphabet = {0, 1}
    tf = dict()

    tf[("z", "lam")] = ["a", "d"]
    tf[("a", "0")] = ["b"]
    tf[("b", 0)] = ["b", "c"]
    tf[("b", 1)] = ["b"]
    tf[("d", "lam")] = ["e", "j"]
    tf[("e", 0)] = ["e"]
    tf[("e", 1)] = ["f"]
    tf[("f", 0)] = ["f", "g"]
    tf[("f", 1)] = ["f"]
    tf[("g", 0)] = ["h"]
    tf[("h", 0)] = ["e"]

    start_state = 'z'
    accept_states = {'j', 'e', 'c'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    test_cases_accept = [[], [0, 1, 1, 0, 0, 0], [
        1, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0]]
    test_case_reject = [[1, 0], [0, 1], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"

    # Test 5 L1 = {LIONS or LMU} alpha = {English Alphabet}
    # Different Alphabet
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    alphabet = set(list(string.ascii_uppercase))
    tf = dict()

    tf[("a", "L")] = ["b"]
    tf[("b", "M")] = ["g"]
    tf[("b", "I")] = ["c"]
    tf[("c", "O")] = ["d"]
    tf[("d", "N")] = ["e"]
    tf[("e", "S")] = ["f"]
    tf[("g", "U")] = ["f"]

    start_state = 'a'
    accept_states = {'f'}

    d = NFA(states, alphabet, tf, start_state, accept_states)

    test_cases_accept = [["L", "I", "O", "N", "S"], ["L", "M", "U"]]
    test_case_reject = [[], ["W", "D", "P"], ["U"], ["L", "M"]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"

    # Test 5 L = {w | w begins with 010 followed by anything and ends with another 0100} alpha = {0, 1}
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

    test_cases_accept = [[0, 1, 0, 0, 1, 0, 0], [
        0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0]]
    test_case_reject = [[0, 0, 1, 0], [1, 0, 1], [1, 1, 1],
                        [0, 1, 1], [], [0, 1, 0, 0, 1, 0, 0, 1]]
    for test in test_case_reject:
        assert d.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert d.run_with_input_list(test) == True, "Should be True"


def nfa_to_dfa_test():

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
    dfa_convert = DFAfromNFA(d)
    dfa = dfa_convert.buildDFA(d)
    test_cases_accept = [[0, 1, 0, 0, 1, 0], [
        0, 1, 0, 0, 0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0]]
    test_case_reject = [[0, 0, 1, 0], [1, 0, 1], [1, 1, 1],
                        [0, 1, 1], [], [0, 1, 0, 0, 1, 0, 0, 1]]
    for test in test_case_reject:
        assert dfa.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert dfa.run_with_input_list(test) == True, "Should be True"

    # assert len(dfa.states) == 10, "Should have 10 states"

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
    dfa_convert = DFAfromNFA(d)
    dfa = dfa_convert.buildDFA(d)
    test_cases_accept = [[0, 1, 0, 0, 1, 0], [
        1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0], [], [1, 1, 1], [0, 0, 0]]
    test_case_reject = [[0, 0, 1, 0], [
        1, 0, 1, 1], [1, 0], [0, 1, 0, 0, 1, 0, 0, 1]]
    for test in test_case_reject:
        assert dfa.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert dfa.run_with_input_list(test) == True, "Should be True"

    # Test 3 L1 = {w | w starts with 0 and ends with 0} alpha = {0, 1} L2 = {w | w is a binary string divisible by 8 and lambda is accepted}... L = L1.L2
    # Multiple Lambda States
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'z'}
    alphabet = {0, 1}
    tf = dict()

    tf[("z", "lam")] = ["a", "d"]
    tf[("a", "0")] = ["b"]
    tf[("b", 0)] = ["b", "c"]
    tf[("b", 1)] = ["b"]
    tf[("d", "lam")] = ["e", "j"]
    tf[("e", 0)] = ["e"]
    tf[("e", 1)] = ["f"]
    tf[("f", 0)] = ["f", "g"]
    tf[("f", 1)] = ["f"]
    tf[("g", 0)] = ["h"]
    tf[("h", 0)] = ["e"]

    start_state = 'z'
    accept_states = {'j', 'e', 'c'}

    d = NFA(states, alphabet, tf, start_state, accept_states)
    dfa_convert = DFAfromNFA(d)
    dfa = dfa_convert.buildDFA(d)

    test_cases_accept = [[], [0, 1, 1, 0, 0, 0], [
        1, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0]]
    test_case_reject = [[1, 0], [0, 1], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0]]
    for test in test_case_reject:
        assert dfa.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert dfa.run_with_input_list(test) == True, "Should be True"

    # Test 4 L1 = {LIONS or LMU} alpha = {English Alphabet}
    # Different Alphabet
    states = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    alphabet = set(list(string.ascii_uppercase))
    tf = dict()

    tf[("a", "L")] = ["b"]
    tf[("b", "M")] = ["g"]
    tf[("b", "I")] = ["c"]
    tf[("c", "O")] = ["d"]
    tf[("d", "N")] = ["e"]
    tf[("e", "S")] = ["f"]
    tf[("g", "U")] = ["f"]

    start_state = 'a'
    accept_states = {'f'}

    d = NFA(states, alphabet, tf, start_state, accept_states)
    dfa_convert = DFAfromNFA(d)
    dfa = dfa_convert.buildDFA(d)

    test_cases_accept = [["L", "I", "O", "N", "S"], ["L", "M", "U"]]
    test_case_reject = [[], ["W", "D", "P"], ["U"], ["L", "M"]]
    for test in test_case_reject:
        assert dfa.run_with_input_list(test) == False, "Should be False"
    for test in test_cases_accept:
        assert dfa.run_with_input_list(test) == True, "Should be True"


if __name__ == "__main__":
    # dfa_min_test()
    # nfa_sim_test()
    nfa_to_dfa_test()
    print("Everything passed")
