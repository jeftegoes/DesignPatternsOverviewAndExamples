from binary_operation import BinaryOperation
from custom_token import CustomToken
from integer import Integer


class Sintax:
    @staticmethod
    def parse(tokens):
        result = BinaryOperation()
        have_lhs = False
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.type == CustomToken.Type.INTEGER:
                integer = Integer(int(token.text))
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
            elif token.type == CustomToken.Type.PLUS:
                result.type = BinaryOperation.Type.ADDITION
            elif token.type == CustomToken.Type.MINUS:
                result.type = BinaryOperation.Type.SUBTRACTION
            elif token.type == CustomToken.Type.LPAREN:  # note: no if for RPAREN
                j = i
                while j < len(tokens):
                    if tokens[j].type == CustomToken.Type.RPAREN:
                        break
                    j += 1
                # preprocess subexpression
                subexpression = tokens[i + 1:j]
                element = Sintax.parse(subexpression)
                if not have_lhs:
                    result.left = element
                    have_lhs = True
                else:
                    result.right = element
                i = j  # advance
            i += 1
        return result
