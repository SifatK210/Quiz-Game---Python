from Database import *

# Welcome message
print("***********************************")
print("Welcome to My Quiz Game !!!")

# Variable to store user score
score = 0


# Function to check whether the user's answer is correct
def check_answer(user_guess, correct_answer):

    if user_guess == correct_answer:
        return True

    else:
        return False


# Loop through all questions in the question bank
for question_num in range(len(question_bank)):

    print("***********************")

    # Display question
    print(question_bank[question_num]["text"])

    # Display options for current question
    for i in options[question_num]:
        print(i)

    # Take user input and convert it to uppercase
    guess = input("Enter your answer(A/B/C/D): ").upper()

    # Check if answer is correct
    is_correct = check_answer(guess, question_bank[question_num]["answer"])

    # If answer is correct
    if is_correct:
        print("Correct Answer")
        score += 1

    # If answer is incorrect
    else:
        print("Incorrect Answer")
        print(f"The correct answer is  {question_bank[question_num]['answer']}")

    # Display current score after each question
    print(f"Your current score is {score}/{question_num + 1}")


# Final result
print(f"You have given {score} correct answers.")

# Calculate percentage score
print(f"Your score is {score/len(question_bank)*100}%")
