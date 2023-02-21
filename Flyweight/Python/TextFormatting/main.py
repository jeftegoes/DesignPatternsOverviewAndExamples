from better_formatted_text import BetterFormattedText
from formatted_text import FormattedText

ft = FormattedText('This is a brave new world')
ft.capitalize(10, 15)
print(ft)

bft = BetterFormattedText('This is a brave new world')
bft.get_range(16, 19).capitalize = True
print(bft)
