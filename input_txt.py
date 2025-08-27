#Read the contents of input.txt
# Step 1: Read the contents of input.txt
with open("input.txt", "r") as f :
    content = f.read()   # 👈 must be indented

# Step 2: Count the number of words
words = content.split()
word_count = len(words)

# Step 3: Convert text to uppercase
uppercase_text = content.upper()

# Step 4: Write processed text + word count to output.txt
with open("output.txt", "w") as f:
    f.write("Processed Text:\n")
    f.write(uppercase_text + "\n")
    f.write(f"\nWord Count: {word_count}\n")
