from list_strategy import ListStrategy


class HtmlListStrategy(ListStrategy):
    def start(self, buffer: list[str]):
        buffer.append("<ul>\n")

    def end(self, buffer: list[str]):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer: list[str], item: str):
        buffer.append(f"    <li>{item}</li>\n")
