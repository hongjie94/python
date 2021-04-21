from cs50 import get_string

text = get_string("Text: ")

nl = ns = 0
nw = 1

for char in text:
    if char.isalpha():
        nl += 1
    if char.isspace():
        nw += 1
    if char in ["?", "!", "."]:
        ns += 1
        
l = (nl/nw) * 100
s = (ns/nw) * 100

index = round(0.0588 * l - 0.296 * s - 15.8)
if (index > 16):
    print("Grade 16+")
elif (index < 1):
    print("Before Grade 1")
else:
    print(f"Grade {index}")