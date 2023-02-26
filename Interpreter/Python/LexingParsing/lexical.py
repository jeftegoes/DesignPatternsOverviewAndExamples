from custom_token import CustomToken


class Lexical:
    @staticmethod
    def lex(input):
        result = []

        i = 0
        while i < len(input):
            if input[i] == '+':
                result.append(CustomToken(CustomToken.Type.PLUS, '+'))
            elif input[i] == '-':
                result.append(CustomToken(CustomToken.Type.MINUS, '-'))
            elif input[i] == '(':
                result.append(CustomToken(CustomToken.Type.LPAREN, '('))
            elif input[i] == ')':
                result.append(CustomToken(CustomToken.Type.RPAREN, ')'))
            else:  # must be a number
                digits = [input[i]]
                for j in range(i + 1, len(input)):
                    if input[j].isdigit():
                        digits.append(input[j])
                        i += 1
                    else:
                        result.append(CustomToken(CustomToken.Type.INTEGER,
                                                  ''.join(digits)))
                        break
            i += 1

        return result
