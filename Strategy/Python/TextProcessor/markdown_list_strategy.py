from list_strategy import ListStrategy


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer: list[str], item: str):
        buffer.append(f" * {item}\n")
