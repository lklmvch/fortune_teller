import random

answers = ["Undoubtedly", "It is bound to be so", "Undeniably", "Definitely yes", "Rest assured", "I think so", "Most likely", "You're on the right way", "The starts say yes", 'Да', "Not quite clear", "Ask later", "Better leave it a secret", "Hard to say", "Focus and ask again", "Don't even think of that", "My answer is no", "The starts say no", "Be mindful of opportunities coming your way", "Trust your intuition; it will guide you"]
print("Hello world, I'm a fortune teller and I know answers to all of your questions")
print("First, please tell me your name")
name = input()
print("Hello", name)
Flag = True
while True:
    input("What's your question? ")
    print(random.choice(answers))
    print("Wanna ask another question? Yes/No ")
    if input().lower() == 'yes':
        Flag = True
    else:
        print("Come back with any questions")
        break
