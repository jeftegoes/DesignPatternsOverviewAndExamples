class HtmlElement:
    indent_size: int = 2

    def __init__(self, name: str = "", text: str = ""):
        self.name: str = name
        self.text: str = text
        self.elements: list = []

    def __str(self, indent: int) -> str:
        lines: list = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    # @staticmethod
    # def create(name):
    #     return HtmlBuilder(name)
