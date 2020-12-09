

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
        # Handles Lambda Moves
        for current in self.current_state:
            if (current, "lam") in self.transition_function.keys():
                for i in self.transition_function[(current, "lam")]:
                    self.current_state += [i]
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
        return self.in_accept_state()


class RegexToNFA:
    """class for building e-nfa from regular expressions"""

    def __init__(self, regex):
        self.star = '*'
        self.plus = '+'
        self.openingBracket = '('
        self.closingBracket = ')'
        self.operators = [self.plus]
        self.regex = regex
        # Possible States, all letters
        self.states = [chr(i) for i in range(65, 91)]
        self.alphabet = [chr(i) for i in range(65, 91)]  # Uppercase Letters
        self.alphabet.extend([chr(i) for i in range(97, 123)])  # Letters
        self.alphabet.extend([chr(i) for i in range(48, 58)])  # Numbers
        self.nfa
        self.tf = dict()

    def getNFA(self):
        return self.nfa

    def buildNFA(self):
        language = set()
        self.stack = []
        self.automata = []
        previous = "::e::"
        count = 0
        for char in self.regex:
            if char in self.alphabet:
                language.add(char)
            elif char == self.openingBracket:
                if previous in self.alphabet or previous in [self.closingBracket, self.star]:
                    self.addOperatorToStack(self.dot)
                self.stack.append(char)
            elif char == self.closingBracket:
                if previous in self.operators:
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous))
                while(1):
                    if len(self.stack) == 0:
                        raise BaseException(
                            "Error processing '%s'. Empty stack" % char)
                    o = self.stack.pop()
                    if o == self.openingBracket:
                        break
                    elif o in self.operators:
                        self.processOperator(o)
            elif char == self.star:
                if previous in self.operators or previous == self.openingBracket or previous == self.star:
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous))
                self.processOperator(char)
            elif char in self.operators:
                if previous in self.operators or previous == self.openingBracket:
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous))
                else:
                    self.addOperatorToStack(char)
            else:
                raise BaseException("Symbol '%s' is not allowed" % char)
            previous = char
        while len(self.stack) != 0:
            op = self.stack.pop()
            self.processOperator(op)
        if len(self.automata) > 1:
            print(self.automata)
            raise BaseException("Regex could not be parsed successfully")
        self.nfa = self.automata.pop()
        self.nfa.language = language

    def addOperatorToStack(self, char):
        while(1):
            if len(self.stack) == 0:
                break
            top = self.stack[len(self.stack)-1]
            if top == self.openingBracket:
                break
            if top == char or top == self.dot:
                op = self.stack.pop()
                self.processOperator(op)
            else:
                break
        self.stack.append(char)

    def processOperator(self, operator):
        if len(self.automata) == 0:
            raise BaseException(
                "Error processing operator '%s'. Stack is empty" % operator)
        if operator == self.star:
            a = self.automata.pop()
            self.automata.append(BuildAutomata.starstruct(a))
        elif operator in self.operators:
            if len(self.automata) < 2:
                raise BaseException(
                    "Error processing operator '%s'. Inadequate operands" % operator)
            a = self.automata.pop()
            b = self.automata.pop()
            if operator == self.plus:
                self.automata.append(BuildAutomata.plusstruct(b, a))
            elif operator == self.dot:
                self.automata.append(BuildAutomata.dotstruct(b, a))


class Automata:
    """class to represent an Automata"""

    def __init__(self, language=set(['0', '1'])):
        self.states = set()
        self.startstate = None
        self.finalstates = []
        self.transitions = dict()
        self.language = language

    @staticmethod
    def epsilon():
        return ":e:"

    def setstartstate(self, state):
        self.startstate = state
        self.states.add(state)

    def addfinalstates(self, state):
        if isinstance(state, int):
            state = [state]
        for s in state:
            if s not in self.finalstates:
                self.finalstates.append(s)

    def addtransition(self, fromstate, tostate, inp):
        if isinstance(inp, str):
            inp = set([inp])
        self.states.add(fromstate)
        self.states.add(tostate)
        if fromstate in self.transitions:
            if tostate in self.transitions[fromstate]:
                self.transitions[fromstate][tostate] = self.transitions[fromstate][tostate].union(
                    inp)
            else:
                self.transitions[fromstate][tostate] = inp
        else:
            self.transitions[fromstate] = {tostate: inp}

    def addtransition_dict(self, transitions):
        for fromstate, tostates in transitions.items():
            for state in tostates:
                self.addtransition(fromstate, state, tostates[state])

    def gettransitions(self, state, key):
        if isinstance(state, int):
            state = [state]
        trstates = set()
        for st in state:
            if st in self.transitions:
                for tns in self.transitions[st]:
                    if key in self.transitions[st][tns]:
                        trstates.add(tns)
        return trstates

    def getEClose(self, findstate):
        allstates = set()
        states = set([findstate])
        while len(states) != 0:
            state = states.pop()
            allstates.add(state)
            if state in self.transitions:
                for tns in self.transitions[state]:
                    if Automata.epsilon() in self.transitions[state][tns] and tns not in allstates:
                        states.add(tns)
        return allstates

    def display(self):
        print("states:", self.states)
        print("start state: ", self.startstate)
        print("final states:", self.finalstates)
        print("transitions:")
        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                for char in tostates[state]:
                    print("  ", fromstate, "->", state, "on '"+char+"'")
            print()

    def getPrintText(self):
        text = "language: {" + ", ".join(self.language) + "}\n"
        text += "states: {" + ", ".join(map(str, self.states)) + "}\n"
        text += "start state: " + str(self.startstate) + "\n"
        text += "final states: {" + \
            ", ".join(map(str, self.finalstates)) + "}\n"
        text += "transitions:\n"
        linecount = 5
        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                for char in tostates[state]:
                    text += "    " + str(fromstate) + " -> " + \
                        str(state) + " on '" + char + "'\n"
                    linecount += 1
        return [text, linecount]

    def newBuildFromNumber(self, startnum):
        translations = {}
        for i in list(self.states):
            translations[i] = startnum
            startnum += 1
        rebuild = Automata(self.language)
        rebuild.setstartstate(translations[self.startstate])
        rebuild.addfinalstates(translations[self.finalstates[0]])
        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                rebuild.addtransition(
                    translations[fromstate], translations[state], tostates[state])
        return [rebuild, startnum]

    def newBuildFromEquivalentStates(self, equivalent, pos):
        rebuild = Automata(self.language)
        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                rebuild.addtransition(
                    pos[fromstate], pos[state], tostates[state])
        rebuild.setstartstate(pos[self.startstate])
        for s in self.finalstates:
            rebuild.addfinalstates(pos[s])
        return rebuild

    def getDotFile(self):
        dotFile = "digraph DFA {\nrankdir=LR\n"
        if len(self.states) != 0:
            dotFile += "root=s1\nstart [shape=point]\nstart->s%d\n" % self.startstate
            for state in self.states:
                if state in self.finalstates:
                    dotFile += "s%d [shape=doublecircle]\n" % state
                else:
                    dotFile += "s%d [shape=circle]\n" % state
            for fromstate, tostates in self.transitions.items():
                for state in tostates:
                    for char in tostates[state]:
                        dotFile += 's%d->s%d [label="%s"]\n' % (
                            fromstate, state, char)
        dotFile += "}"
        return dotFile


class BuildAutomata:
    """class for building e-nfa basic structures"""

    @staticmethod
    def basicstruct(inp):
        state1 = 1
        state2 = 2
        basic = Automata()
        basic.setstartstate(state1)
        basic.addfinalstates(state2)
        basic.addtransition(1, 2, inp)
        return basic

    @staticmethod
    def plusstruct(a, b):
        [a, m1] = a.newBuildFromNumber(2)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2
        plus = Automata()
        plus.setstartstate(state1)
        plus.addfinalstates(state2)
        plus.addtransition(plus.startstate, a.startstate, Automata.epsilon())
        plus.addtransition(plus.startstate, b.startstate, Automata.epsilon())
        plus.addtransition(
            a.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.addtransition(
            b.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.addtransition_dict(a.transitions)
        plus.addtransition_dict(b.transitions)
        return plus

    @staticmethod
    def dotstruct(a, b):
        [a, m1] = a.newBuildFromNumber(1)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2-1
        dot = Automata()
        dot.setstartstate(state1)
        dot.addfinalstates(state2)
        dot.addtransition(a.finalstates[0], b.startstate, Automata.epsilon())
        dot.addtransition_dict(a.transitions)
        dot.addtransition_dict(b.transitions)
        return dot

    @staticmethod
    def starstruct(a):
        [a, m1] = a.newBuildFromNumber(2)
        state1 = 1
        state2 = m1
        star = Automata()
        star.setstartstate(state1)
        star.addfinalstates(state2)
        star.addtransition(star.startstate, a.startstate, Automata.epsilon())
        star.addtransition(
            star.startstate, star.finalstates[0], Automata.epsilon())
        star.addtransition(
            a.finalstates[0], star.finalstates[0], Automata.epsilon())
        star.addtransition(a.finalstates[0], a.startstate, Automata.epsilon())
        star.addtransition_dict(a.transitions)
        return star
