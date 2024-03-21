# Define the main function to run the program
def main():
    # Ask the user to input a text
    text = input("Text: ")

    # Calculate the readability grade of the text
    grade = calculate_grade(text)

    # Display the calculated grade
    print_grade(grade)


# Function to calculate the Coleman-Liau readability index
def calculate_grade(text):
    # Initialize counters for letters, words, and sentences
    letters = 0
    words = 0
    sentences = 0

    # Loop through each character in the text
    for char in text:
        # Count letters (alphabetic characters)
        if char.isalpha():
            letters += 1
        # Count words (whitespace separates words)
        elif char.isspace():
            words += 1
        # Count sentences (periods, exclamation marks, and question marks)
        elif char in [".", "!", "?"]:
            sentences += 1

    # Calculate the average number of letters and sentences per 100 words
    L = letters / (words + 1) * 100
    S = sentences / (words + 1) * 100

    # Calculate the Coleman-Liau index
    index = round(0.0588 * L - 0.296 * S - 15.8)

    return index


# Function to print the readability grade based on the index
def print_grade(grade):
    if grade < 1:
        # If the grade is less than 1, it's considered "Before Grade 1"
        print("Before Grade 1")
    elif grade >= 16:
        # If the grade is 16 or higher, it's "Grade 16+"
        print("Grade 16+")
    else:
        # Otherwise, print the calculated grade
        print(f"Grade {grade}")


# Ensure the main function is executed when the script is run
main()
