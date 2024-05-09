print('\n---------- Welcome to our quiz game ----------\n')
playing = input('Do you want to play? ').lower()
if playing != 'yes':
    quit()

print("Okay, let's play!")
questions = {
    "What is the capital of France?": "paris",
    "What is the largest planet in our solar system?": "jupiter",
    "Who wrote 'Romeo and Juliet'?": "william shakespeare",
    "What is the capital of Morocco?": "rabat",
    "Who painted the Mona Lisa?": "leonardo da vinci"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

print(f'Your final score is {score} / {len(questions)}')