from lexical import Lexical
from sintax import Sintax


def eval(input):
    tokens = Lexical.lex(input)
    print(' '.join(map(str, tokens)))

    parsed = Sintax.parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(13+4)-(12+1)')
    eval('1+(3-4)')

    # this won't work
    eval('1+2+(3-4)')
