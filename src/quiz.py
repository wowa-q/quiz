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
    "What's one effect of calling renadmo.seed(42)": [
        "The random numbers are reproduceable",
        "The random numbers are more random",
        "The computer clock is reset",
        "The first random number is always 42",
    ],
    "When does __name__ == '__main__' equal True in a python file": [
        "When the file is run as a script",
        "When the file is imported as a module",
        "When the file has a valid name",
        "When the file only has one function",
    ]
}

def prepare_questions(questions, num_questions):
    '''
    @questions is the data structure containing the questions
    @num_questions is the number of questions
    '''
    num_questions = min(num_questions,len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def ask_question(question, alternatives):
    ''' 
    Helper function, which is called in the main loop to ask a question
    '''
    # the first answer in the list of alternatives is correct
    correct_answer = alternatives[0]
    # the answers will be returned in a random order random.sample creates new list
    # instead of random.shuffle would shuffle the values inside of the existing list
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else: 
        print(f"The answer is {correct_answer!r} not {answer!r}")
        return 0

def get_answer(question, alternatives):
    ''' 
    Another heloer function
    @question is the question text
    @alternatives is a list of alternatives
    '''
    print(f"{question}?")
    # combine letters and alternatives with zip() and store them sorted in a dictionary 
    # random is mixing the values in the list of labeled alternatives before it will be ziped - see ask_question()
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    # dispays the alternatives with the labels (they were ziped)
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")
    
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def run_quiz():
    ''' 
    Is the main loop of the quiz.
    '''
    questions = prepare_questions(QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ)
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\ You got {num_correct} correct out of {num} questions")
    
    
if __name__ == "__main__":
    run_quiz()