from copy import deepcopy

from custom_token import CustomToken
from memento import Memento


class TokenMachine:
    def __init__(self):
        self.custom_tokens: CustomToken = []

    def add_token_value(self, value):
        return self.add_token(CustomToken(value))

    def add_token(self, token):
        self.custom_tokens.append(token)
        return Memento(deepcopy(self.custom_tokens))

    def revert(self, memento):
        self.custom_tokens = [CustomToken(x.value) for x in memento]
