def count_words(text):
    """
    Counts the number of words in a given text.
    :param text: String containing the sentence or paragraph input by the user.
    :return: Integer representing the number of words in the input text.
    """
    # Check if the input is not empty
    if not text.strip():
        return "The input text is empty. Please enter a valid sentence or paragraph."
    
    # Split the text into words and count them
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Count the words in the input
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"The number of words in your input is: {word_count}")

if __name__ == "__main__":
    main()
