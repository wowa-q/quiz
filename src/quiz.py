''' executed Step 2, continue with step 3'''
import random
import tomli
import pathlib
from string import ascii_lowercase  #ascii_lowercase to get letters that label the answer alternatives

NUM_QUESTIONS_PER_QUIZ = 50
# with __file__ parameter starts to search in the same directory as quiz.py
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
# read the text form toml and parse it into a dict
QUESTIONS = tomli.loads(QUESTIONS_PATH.read_text())

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