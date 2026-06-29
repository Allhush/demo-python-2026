x = 0
text = input("what is the most recent fruit you ate? ");
for i in text:
        if i == "a":
            text = str.replace(text, text[x], "b")
        x += 1;

print(text);