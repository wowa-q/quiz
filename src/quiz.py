''' executed Step 2, continue with step 3'''
import random
from string import ascii_lowercase  #ascii_lowercase to get letters that label the answer alternatives
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
# the questions will be returned in a random order random.sample creates new list
# instead of random.shuffle would shuffle the values inside of the existing list
questions = random.sample(list(QUESTIONS.items()), k=num_questions)
num_correct = 0

for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    # the first answer in the list of alternatives is correct
    correct_answer = alternatives[0]
    # combine letters and alternatives with zip() and store them sorted in a dictionary 
    # random is mixing the values in the list of labeled alternatives before it will be ziped
    labeled_alternatives=dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    # dispays the alternatives with the labels (they were ziped)
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")
    
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of  {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer: 
        num_correct += 1
        print("Correct!")
    else: print(f"The answer is {correct_answer}, not {answer!r}")   

print(f"\nYou got {num_correct} correct out of {num} questions")