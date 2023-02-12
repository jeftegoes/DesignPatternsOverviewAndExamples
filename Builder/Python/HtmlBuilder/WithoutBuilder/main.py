text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

words = ["hello", "world"]
parts = ["<ul>"]
for word in words:
    parts.append(f" <li>{word}</li>")
parts.append("</ul>")
print("\n".join(parts))
