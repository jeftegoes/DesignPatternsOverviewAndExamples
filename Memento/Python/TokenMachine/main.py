from token_machine import TokenMachine

token_machine = TokenMachine()
m = token_machine.add_token_value(123)
token_machine.add_token_value(456)
token_machine.revert(m)

print(len(token_machine.custom_tokens))
print(token_machine.custom_tokens[0].value)