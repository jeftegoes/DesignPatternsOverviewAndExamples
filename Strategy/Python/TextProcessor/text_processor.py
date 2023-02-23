from html_list_strategy import HtmlListStrategy
from list_strategy import ListStrategy
from markdown_list_strategy import MarkdownListStrategy
from output_format import OutputFormat


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HtmlListStrategy()) -> None:
        self.buffer: list[str] = []
        self.list_strategy = list_strategy

    def append_list(self, items: list[str]):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format: OutputFormat):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self) -> str:
        return "".join(self.buffer)
