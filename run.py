import time

# Introduces the game and prompts user to create a username.

print("Hi! I'm QuizBot. Create a username to start.")
print("---------------------------------")
username = input("Username: ")
print("---------------------------------")
print(f"Hey, {username}! Are you ready to test your knowledge of countries?")
print("---------------------------------")
print("Note: answers should be 'a', 'b', or 'c' in lowercase. 'True/False' to be answered as 't/f'")

# Checks to see whether user wants to start quiz or not

start_quiz = input("Type 'y' or 'n' to start: ")

if start_quiz == "y":
    print("Brilliant! Get your quiz hat on!")
    time.sleep(1)
    print("Hang on a sec whilst I think of what questions to ask you...")
    time.sleep(1)
    print("Ok, ready? No pressure but I thought it'd be fun to time you as well. Good luck!")
    print("---------------------------------")
    time.sleep(2)
else:
    print("Oh... I guess this is goodbye then :(")
    raise SystemExit()


# class for loop
class Quiz:
    """
    create variable to be called and manipulated to check which question is called, and the corresponding answer.
    """
    def __init__(self, asked, answer):
        self.asked = asked
        self.answer = answer


# questions to be asked and multiple choise answers
question_asked = [
    "1)The longest coastline in the world belongs to which country?\n a) Canada\n b) Mexico\n c) Australia\n d) South Africa\n",
    "2) By size, which is the smallest country in The world?\n a) Haiti\n b) Nauru\n c) Vatican City\n d) Monaco\n",
    "3) The unicorn is the national animal of which country?\n a) Ireland\n b) Scotland\n c) England\n d) Wales\n",
    "4) Where would you find the world\'s tallest building?\n a) Dubai\n b) UAE\n c) France\n d) America\n",
    "5) Officially, the hottest country in the world is...\n a) Mali\n b) Tuvalu\n c) Djibouti\n d) Malta\n",
    "6) ...And the coldest country?\n a) Russia\n b) Iceland\n c) Norway\n d) Antarctica\n",
    "7) Beirut is the capital of:\n a) Isreal\n b) Syria\n c) Lebanon\n d) Jordan\n",
    "8) True or false: Russia has a larger surface area than Pluto?\n true (t)\n false (f)\n",
    "9) Where would you find the Bay of Pigs?\n a) Maldives\n b) Hawaii\n c) Cuba\n d) Dominican Republic\n",
    "10) Finally, Sicily is home to which mountain?\n a) Mt Everest\n b) Mt Etna\n c) K2\n d) Kilimanjaro\n"
    ]

# starts timer
start_time = time.time()

# questions asked with their corresponding answers
questions = [
    Quiz(question_asked[0], "a"),
    Quiz(question_asked[1], "c"),
    Quiz(question_asked[2], "b"),
    Quiz(question_asked[3], "a"),
    Quiz(question_asked[4], "c"),
    Quiz(question_asked[5], "a"),
    Quiz(question_asked[6], "c"),
    Quiz(question_asked[7], "t"),
    Quiz(question_asked[8], "c"),
    Quiz(question_asked[9], "b")
]


# function to loop between the questions and counts score, increments of +1 if answer is correct.
def run_quiz(questions):
    """
    defines score variable, set to 0
    Uses 'for' loop to cycle between questions in order they're written.
    Checks user's input for answer and compares against question's answer.
    Increments score by +1 if answer is correct.
    Displays user's score out of 10
    """
    score = 0
    for question in questions:
        answer = input(question.asked)
        if answer == question.answer:
            score += 1
            # stops timer
            end_time = time.time()
            duration = int(end_time - start_time)
    print("Congrats! You scored ", score, "/", len(questions), "in", duration, "seconds")


"""
Differntiate between different score brackets
total_score = score
if score > 8:
    print("Whoa, look at you being a master mind")
elif score > 5:
    print("Okay okay, your knowledge exceeded my expectations")
else:
    print("Not quite there yet - keep revising!")
    print("---------------------------------")
"""

# runs quiz and prints UI to terminal
run_quiz(questions)

# sets an input variable for the end user to interact to either restart the quiz or not
restart_quiz = input("Thanks for playing! Is your knowledge as good as you thought?\n\
     To play again, press 'r', if not 'x':\n")
print("---------------------------------")

# restart quiz
if restart_quiz == "r":
    start_time = time.time()
    run_quiz(questions)
else:
    print("Goodbye, Quizbot out!")
    raise SystemExit()
