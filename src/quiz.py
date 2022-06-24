''' executed Step 2, continue with step 3'''
import random
import tomli
import pathlib
from string import ascii_lowercase  #ascii_lowercase to get letters that label the answer alternatives

NUM_QUESTIONS_PER_QUIZ = 5
# with __file__ parameter starts to search in the same directory as quiz.py
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def prepare_questions(path, num_questions):
    '''
    @path path to the TOML file with the questions
    @num_questions is the number of questions
    '''
    # read the text form toml and parse it into a dict
    topic_info = tomli.loads(path.read_text())
    # get get all question from the toml file, labeled by the topic label
    # topics is a dict with "label":"question" pairs
    topics = {
        topic["label"]: topic["questions"] for topic in topic_info.values()
    }
    # use the helper function to ask which topic is to use - only one answer is possible
    topic_label = get_answers(
        question="Which topic do you want to be quizzed about",
        # sort the dict by topic
        alternatives=sorted(topics),
    )[0]
    questions = topics[topic_label]

    num_questions = min(num_questions,len(questions))
    return random.sample(list(questions), k=num_questions)

def ask_question(question):
    ''' 
    Helper function, which is called in the main loop to ask a question
    '''
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    # the answers will be returned in a random order random.sample creates new list
    # instead of random.shuffle would shuffle the values inside of the existing list
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"], 
        alternatives=ordered_alternatives, 
        num_choices=len(correct_answers),
        hint=question.get("hint"), # use get, since not all questions have a hint and avoid key error
    )
    if correct := set(answers) == set(correct_answers):
        print("⭐ Correct! ⭐")
        
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer {is_or_are}:"] + correct_answers))
        
    if "explanation" in question:
        print(f"\nEXPLANATION: \n{question['explanation']}")
    
    return 1 if correct else 0

def get_answers(question, alternatives, num_choices=1, hint=None):
    """
    Another helper function
    @question is the question item from question.toml
    @alternatives is a list of alternatives
    @num_choices is the number of correct answers
    returns a list of strings
    """
    print(f"{question}?")
    # combine letters and alternatives with zip() and store them in a dictionary 
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    # add a label for a hint
    if hint:
        labeled_alternatives["?"] = "hint"

    # dispays the alternatives with the labels (they were ziped)
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative} ")

    while True:
        # put the answers into plural_s for further checks
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        # put answers to a set to quickly ignore duplicate alternatives. An answer string like "a, b, a" is interpreted as {"a", "b"}.
        answers = set(answer.replace(",", " ").split())
        # handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # handle invalid answers
        # check the given number of answers compared to choices 
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue
        # check if the given answers are contained in the labels
        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not valid choice. "
                f"please use {', '.join(labeled_alternatives)}"
            )
            continue
        return [labeled_alternatives[answer] for answer in answers]

def run_quiz():
    ''' 
    Is the main loop of the quiz.
    '''
    questions = prepare_questions(QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ)
    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\ You got {num_correct} correct out of {num} questions")
    

if __name__ == "__main__":
    run_quiz()