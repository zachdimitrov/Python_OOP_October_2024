def reverse_text(text):
    idx = len(text) - 1
    while idx >= 0:
        yield text[idx]
        idx -= 1


print("".join(reverse_text("proba")))
for char in reverse_text("step"):
    print(char, end='')
