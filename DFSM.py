from typing import Set, Dict, Tuple


class DFSM:
    """Deterministic Finite State Machine"""
    def __init__(self, states: Set[int],
                       alphabet: Set[str],
                       starting_state: int,
                       transitions: Dict[Tuple[int, str]: int],
                       final_states: Set[int]) -> None:
        self.states = states
        self.alphabet = alphabet
        self.starting_state = starting_state
        self.transitions = transitions
        self.final_states = final_states
        self.state = self.starting_state
        assert [(q, s) for q in states for s in alphabet] == list(self.transitions.keys())

    def __call__(self, s: str) -> bool:
        accept = False
        if not (set(s) <= self.alphabet):
            print(f"The string s = '{s}' contains symbols which are not in this state machine's alphabet {self.alphabet}.")
        else:
            for char in s:
                self.state = self.transitions[(self.state, char)]
            if self.state in self.final_states:
                accept = True
            self.state = self.starting_state
        return accept
