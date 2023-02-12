from html_element import HtmlElement


class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name: str = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name: str, child_text: str):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self) -> None:
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self) -> str:
        return str(self.__root)
