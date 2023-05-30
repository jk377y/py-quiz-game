# module is imported because it is used to load the quiz questions from a JSON file
import json
# used to randomly select 10 questions from the quiz
import random

# function to display the question and choices
def display_question(question, choices):
    # Display the question
    print(question)
    # Display the choices (with a number for each choice starting at 1) 
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

# function to get the user's choice
def get_user_choice(num_choices):
    while True:
        # Get the user's choice and validates it (should be a number between 1 and the number of choices)
        choice = input("Enter your answer choice (1-{}): ".format(num_choices))
        if choice.isdigit() and 1 <= int(choice) <= num_choices:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

# load the quiz questions from the JSON file questions.json and stores them in a variable called questions
with open('questions.json') as file:
    questions = json.load(file)

# function to run the quiz game
def quiz_game():
    
    # Initialize the score to 0
    score = 0

    print("=== Quiz Game ===")
    print("Answer the following questions:")

    # Select 10 questions randomly from the list of questions using the random.sample() function and stores them in a variable called selected_questions
    selected_questions = random.sample(questions, 10)

    # Loop through the selected questions
    for question in selected_questions:
        # Display the question and choices
        display_question(question["question"], question["choices"])
        # Get the user's choice
        user_choice = get_user_choice(len(question["choices"]))

        # Check if the user's choice is correct; adds green color to the text if correct
        if user_choice == question["correct_choice"]:
            print("\033[92mCorrect!\033[0m")
            # Increment the score by 1
            score += 1
        # If the user's choice is incorrect, display the correct answer; adds red color to the text if incorrect
        else:
            print("\033[91mIncorrect!\033[0m")
            print(f"The correct answer is: {question['choices'][question['correct_choice']-1]}")

        # Print a blank line to separate the questions; should loop back to the beginning of the loop until all the selected questions have been asked
        print()

    # when all the selected questions have been asked, display the final score and percentage
    print("Quiz completed!")
    print("Your score: {}/{} ({:.2f}%)".format(score, len(selected_questions), (score / len(selected_questions)) * 100))

# Run the quiz game
quiz_game()