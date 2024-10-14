from output_format import OutputFormat
from text_processor import TextProcessor

items: list[str] = ["foo", "bar", "baz"]

text_processor = TextProcessor()
text_processor.set_output_format(OutputFormat.MARKDOWN)
text_processor.append_list(items)
print(text_processor)

text_processor.set_output_format(OutputFormat.HTML)
text_processor.clear()
text_processor.append_list(items)
print(text_processor)
