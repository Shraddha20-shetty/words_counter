def count_words(text):
    # Split the text into words using whitespace as the separator
    words = text.split()
    # Return the number of words
    return len(words)
# Prompt the user for input
user_input = input("Enter your text: ")
# Count the number of words
word_count = count_words(user_input)
# Display the word count
print(f"Word Count: {word_count}")