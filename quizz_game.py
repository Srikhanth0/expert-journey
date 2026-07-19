quiz = {
    "what is the capital of tamilnadu" : "Chennai".lower(),
    "what is the national animal of india" : "Tiger".lower(),
    "'what is the famous place in chennai" : "marina beach".lower()
}

score=0

for question,answer in quiz.items():
    print(question)

    while True:

        user_guesses = input("what is your answer?")

        if answer in user_guesses.lower():
            print("correct")
            score+=1
            next_question = input("wanna continue?, type 'yes' to continue and 'no' to quit")
            print(next_question)
            if next_question.lower() == "yes":
                break

            elif next_question.lower() == "no":
                quit()

        elif answer not in user_guesses.lower():
            try_again = input("it's wrong, do you want to try again?, type 'yes' to continue and 'no' to quit")
            print(try_again)
            if try_again.lower() == "yes":
                pass

            elif try_again.lower() == "no":
             quit()

            else:
                pass

print(f"game over, your score is {score}")
